from django.urls import reverse
from ..models import Versement, Contrat,Client
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.db.models import Q

from datetime import date

def save_transaction(request):
    if request.method == "POST":
        try:
            montant_versement = request.POST["montant_versement"]
            date_versement = request.POST["date_versement"]
            contrat = request.POST["contrat"]
            note = request.POST["note"]  
            contrat_obj = Contrat.objects.get(client=Client.objects.get(nom=contrat))
            Versement.objects.create(montant_versement=montant_versement, date_versement=date_versement, contrat=contrat_obj, note=note)
            return HttpResponseRedirect(reverse("askia_admin:transaction_form"))
        except Contrat.DoesNotExist:
            print("Contrat does not exist")
        except Exception as e:
            print("Error:", e)

    # Handle GET request or any other scenario where POST method isn't used
    return HttpResponseRedirect(reverse("askia_admin:transaction_form"))



# formulaire de création d'une transaction#
def transaction_form(request):
     # Obtenir la date actuelle
    date_actuelle = date.today().isoformat()
    contrats = Contrat.objects.all()
    
    context = {
        'date_actuelle': date_actuelle,
        'contrats':contrats
    }
    return render(request,"transactions/create.html", context)
# transactions liste
def transaction_list(request):
    return render(request,"transactions/liste.html")





@csrf_protect
def transaction_list(request):
    if request.method == "POST":
        print('******yes')
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        search = request.POST.get('search[value]')
        date_from = request.POST.get('from_date', None)
        date_to = request.POST.get('to_date', None)

        if date_from is not None:
            # Filter data based on date range
            filtered_transactions = Versement.objects.filter(
                Q(montant_versement__icontains=search) | Q(montant_total_paye__icontains=search) | Q(
                    note__icontains=search),
                date_versement__range=[date_from + " 00:00:00", date_to + " 23:59:59"]
            )[start:start + length]
        else:
            # Filter data without date range
             filtered_transactions = Versement.objects.filter(
                Q(montant_versement__icontains=search) | Q(montant_total_paye__icontains=search) | Q(
                    note__icontains=search)
            )[start:start + length]

        data = {
            "draw": draw,
            "recordsTotal": Versement.objects.count(),
            "recordsFiltered": filtered_transactions.count(),
            "data": [{
                "id": versement.id,
                "nom": versement.contrat.client.nom,
                "contact": versement.contrat.client.contact,
                "date_versement": versement.date_versement,
                "montant_versement": versement.montant_versement,
                "montant_total_paye": versement.montant_total_paye,
                "montant_a_paye": versement.contrat.montant_contrat,
                "reste": f"{versement.contrat.montant_contrat - versement.montant_total_paye}",
                "note": versement.note,
              
            } for versement in filtered_transactions]
        }

        return JsonResponse(data)

    return render(request, 'transactions/liste.html')


