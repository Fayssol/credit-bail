from django.urls import reverse
from ..models import Versement, Contrat
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse

from datetime import date


# sauvegarde d'une transaction#
def save_transaction(request):
     if request.method == "POST":
        try:
            montant_versement = request.POST["montant_versement"]
            date_versement = request.POST["date_versement"]
            contrat = request.POST["contrat"]
            note = request.POST["contrat"]

        except:
            print("error recuperation")
        else:
            try:
                
                Versement.objects.create(montant_versement=montant_versement, date_versement=date_versement, contrat=contrat,note=note)
                # return HttpResponseRedirect("/transaction_form")
                return HttpResponseRedirect(reverse("askia_admin:transaction_form"))
            except:
                print("error save")


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




