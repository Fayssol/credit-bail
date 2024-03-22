from django.urls import reverse
from ..models import Versement, Contrat,Client
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse

from datetime import date


# sauvegarde d'une transaction#
# def save_transaction(request):
#      if request.method == "POST":
#         try:
#             montant_versement = request.POST["montant_versement"]
#             date_versement = request.POST["date_versement"]
#             contrat = request.POST["contrat"]
#             note = request.POST["contrat"]

#         except:
#             print("error recuperation")
#         else:
#             try:
#                 contrat_id = Contrat.objects.get(nom=contrat)
#                 Versement.objects.create(montant_versement=montant_versement, date_versement=date_versement, contrat=contrat_id,note=note)
#                 # return HttpResponseRedirect("/transaction_form")
#                 return HttpResponseRedirect(reverse("askia_admin:transaction_form"))
#             except:
#                 print("error save")

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




