<<<<<<< HEAD
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .vues.transactions_views import *
from .vues.client_views import *
from .models import Contrat, Versement
=======
from django.shortcuts import render,HttpResponse,redirect
>>>>>>> c401a84af74c0b031721cb83d3be714e3d458c51

# Create your views here.


def base(request):
    return render(request,'layouts/base.html')

<<<<<<< HEAD
=======
def create(request):
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
>>>>>>> c401a84af74c0b031721cb83d3be714e3d458c51


        ## save et validator##
        return redirect("/create")
    else:
        return render(request,'clients/create.html')
def index(request):
    return HttpResponse("Welcome")




