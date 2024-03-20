from ..models import Versement, Contrat
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse

# formulaire de création d'un client#
def client_form(request):
    return render(request,'clients/create.html')

def client_liste(request):
    return render(request,'clients/liste.html')


def create_client(request):
    if request.method=='POST':
        #client
        nom=request.POST.get('nom')
        contact=request.POST.get('contact')
        adresse=request.POST.get('adresse')
        date_naiss=request.POST.get('date_naissance')
        ####contrat
        montant=request.POST.get('montant')
        duree=request.POST.get('duree')
        date_signature=request.POST.get('date_sgnture')
        ###temoin
        nomTemoin=request.POST.get('nomTemoin')
        adresseTemoin=request.POST.get('adresseTemoin')
        contact=request.POST.get('contactTemoin')
        #date_naiss=request.POST.get('date_naissance')
        print("request: \n")
        print(request.POST)



        ## save et validator##
        return redirect("/create")
    else:
        return render(request,'clients/create.html')
    