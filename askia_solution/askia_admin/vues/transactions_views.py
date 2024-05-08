from django.urls import reverse
from ..models import Versement, Contrat,Client
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.db.models import Q

from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def save_transaction(request):

    msg_vers_depasse = False
    if request.method == "POST":
        submission_url = request.path
        print(submission_url)
        contrats = Contrat.objects.filter(etat="EN_COURS").all()
        date_actuelle =  date.today().isoformat()

        try:
            montant_versement = request.POST["montant_versement"]
            date_versement = request.POST["date_versement"]
            contrat = request.POST["contrat"]
            note = request.POST["note"]  
            contrat_obj = Contrat.objects.get(client=Client.objects.get(nom=contrat))
            # Avant de creer un versement il faut verifier que le versement ne va pas exceder
            try:
                paye = contrat_obj.versement_set.last().montant_total_paye
            except:
                paye = 0    
            a_paye = contrat_obj.montant_contrat
            reste_a_paye = a_paye - paye
            if int(montant_versement) <= reste_a_paye:
                 print("oui inferieur******************")
                 Versement.objects.create(montant_versement=montant_versement, date_versement=date_versement, contrat=contrat_obj, note=note)
                 paye_apres_vers = contrat_obj.versement_set.last().montant_total_paye
                 if int(paye_apres_vers) == int(a_paye):
                  
                     contrat_obj.etat = "TERMINE"
                   
                     contrat_obj.save()
                   
           
                 if submission_url == '/transaction_modal/':
                   
                    return HttpResponseRedirect(reverse("askia_admin:transaction_index"), {"reste":reste_a_paye,"msg":msg_vers_depasse})
                
                 HttpResponseRedirect(reverse("askia_admin:transaction_form"), {"reste":reste_a_paye, "msg":msg_vers_depasse})
            else:
                
                 msg_vers_depasse = True

           
                 if submission_url == '/transaction_modal/':
                  
                    # return HttpResponseRedirect(reverse("askia_admin:transaction_index"), {"reste":reste_a_paye,"msg":msg_vers_depasse})
                    return render(request,"transactions/liste.html",{"reste":reste_a_paye,"msg":msg_vers_depasse, "date_actuelle":date_actuelle,"contrats":contrats})
                
                #  HttpResponseRedirect(reverse("askia_admin:transaction_form"), {"reste":reste_a_paye, "msg":msg_vers_depasse})
                 return render(request,"transactions/create.html",{"reste":reste_a_paye,"msg":msg_vers_depasse, "date_actuelle":date_actuelle})

        except Contrat.DoesNotExist:
            print("Contrat does not exist")
        except Exception as e:
            print("Error:", e)
   
    return HttpResponseRedirect(reverse("askia_admin:transaction_form"))




# formulaire de création d'une transaction#
def transaction_form(request):
     # Obtenir la date actuelle
    date_actuelle = date.today().isoformat()
    contrats = Contrat.objects.filter(etat="ENCOURS").all()
    # date_actuelle =  date_actuelle,
    # contrats = contrats
    # context = {
    #     'date_actuelle': date_actuelle,
    #     'contrats':contrats
    # }
    return render(request,"transactions/create.html", locals())

# transactions liste
def transaction_index(request):
    date_actuelle = date.today().isoformat()
    contrats =  contrats = Contrat.objects.filter(etat="ENCOURS").all()

    return render(request,"transactions/liste.html",{'contrats': contrats, 'date_actuelle': date_actuelle})


@csrf_protect
def transaction_list(request):
    if request.method == "POST":
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        search = request.POST.get('search[value]')
        date_from = request.POST.get('from_date', None)
        date_to = request.POST.get('to_date', None)
        id=request.POST.get('id')
        
        filtered_transactions = Versement.objects.order_by('-date_versement', '-id')
        url="ajax_transaction_list_contrat"
        if (request.path== url):
            filtered_transactions = Versement.objects.filter(id=id).order_by('-date_versement', '-id')
        else:
            filtered_transactions = Versement.objects.order_by('-date_versement', '-id')

        if search:
            filtered_transactions = filtered_transactions.filter(
                Q(montant_versement__icontains=search) |
                Q(montant_total_paye__icontains=search) |
                Q(note__icontains=search) |
                Q(date_versement__icontains=search) |
                Q(contrat__montant_contrat__icontains=search) |
                Q(contrat__client__nom__icontains=search) |  
                Q(contrat__client__contact__icontains=search) 
            )
        if date_from and date_to:
            filtered_transactions = filtered_transactions.filter(
                date_versement__range=[date_from , date_to ]
            )

        
        if (request.path== url):
            contrat_courant=Contrat.objects.get(id=id)
            total_records = Versement.objects.filter(contrat=contrat_courant).count()
        else:
            total_records = Versement.objects.count()
        total_filtered_records = filtered_transactions.count()


        data = {
            "draw": draw,
            "recordsTotal": total_records,
            "recordsFiltered": total_filtered_records,
            "data": [{
                "nom": versement.contrat.client.nom,
                "contact": versement.contrat.client.contact,
                "date_versement": versement.date_versement.strftime('%Y-%m-%d'),  
                "montant_versement": '{:,.0f}'.format(versement.montant_versement).replace(',', ' '), 
                "montant_total_paye": '{:,.0f}'.format(versement.montant_total_paye).replace(',', ' '),
                "montant_contrat": '{:,.0f}'.format(versement.contrat.montant_contrat).replace(',', ' '),
                "reste": '{:,.0f}'.format(versement.contrat.montant_contrat - versement.montant_total_paye).replace(',', ' '),
                "note": versement.note,
            } for versement in filtered_transactions[start:start + length]],
            
        }

        return JsonResponse(data)
    

    return render(request, 'transactions/liste.html')


