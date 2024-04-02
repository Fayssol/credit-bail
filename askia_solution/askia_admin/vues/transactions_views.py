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
    msg = False 
    if request.method == "POST":
        try:
            montant_versement = request.POST["montant_versement"]
            date_versement = request.POST["date_versement"]
            contrat = request.POST["contrat"]
            note = request.POST["note"]  
            contrat_obj = Contrat.objects.get(client=Client.objects.get(nom=contrat))
            Versement.objects.create(montant_versement=montant_versement, date_versement=date_versement, contrat=contrat_obj, note=note)
            print("*************oui")
            msg = True  # Définir msg à True si la transaction est réussie
            
            return HttpResponseRedirect(reverse("askia_admin:transaction_form"), locals())
        except Contrat.DoesNotExist:
            print("Contrat does not exist")
        except Exception as e:
            print("Error:", e)
    print("*********Non")
    return HttpResponseRedirect(reverse("askia_admin:transaction_form"), {"msg": msg})




# formulaire de création d'une transaction#
def transaction_form(request):
     # Obtenir la date actuelle
    date_actuelle = date.today().isoformat()
    contrats = Contrat.objects.all()
    # date_actuelle =  date_actuelle,
    # contrats = contrats
    # context = {
    #     'date_actuelle': date_actuelle,
    #     'contrats':contrats
    # }
    return render(request,"transactions/create.html", locals())

# transactions liste
def transaction_list(request):
    return render(request,"transactions/liste.html")



from django.db.models import Q

@csrf_protect
def transaction_list(request):
    if request.method == "POST":
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        search = request.POST.get('search[value]')
        date_from = request.POST.get('from_date', None)
        date_to = request.POST.get('to_date', None)

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

        total_records = Versement.objects.count()
        total_filtered_records = filtered_transactions.count()

        data = {
            "draw": draw,
            "recordsTotal": total_records,
            "recordsFiltered": total_filtered_records,
            "data": [{
                # "id": versement.id,
                "nom": versement.contrat.client.nom,
                "contact": versement.contrat.client.contact,
                "date_versement": versement.date_versement,
                "montant_versement": versement.montant_versement,
                "montant_total_paye": versement.montant_total_paye,
                "montant_contrat": versement.contrat.montant_contrat,
                "reste": f"{versement.contrat.montant_contrat - versement.montant_total_paye}",
                "note": versement.note,
            } for versement in filtered_transactions[start:start + length]]
        }

        return JsonResponse(data)

    return render(request, 'transactions/liste.html')


