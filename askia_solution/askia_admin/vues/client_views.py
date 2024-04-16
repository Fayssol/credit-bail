from ..models import Versement,Client,Temoin,Contrat
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
# formulaire de création d'un contrat#
def contrat_form(request):
   
    return render(request,'contrats/create.html')

# def client_liste(request):
#     return render(request,'clients/liste.html')


def save_contrat(request):

    if request.method=='POST':
        #validator
        #client infos
        nom=request.POST.get('nom')
        contact=request.POST.get('contact')
        adress=request.POST.get('adresse')
        date_naiss=request.POST.get('date_naissance')
        #instance
        clt=Client(nom=nom,contact=contact,adresse=adress,date_naissance=date_naiss)
        clt.save()
        ####contrat infos
        montant=request.POST.get('montant')
        duree=request.POST.get('duree')
        date=request.POST.get('date_sgnture')
        #instance
        contrat=Contrat(montant_contrat=montant,date_contrat=date,duree=duree,client=clt)
        contrat.save()
        ###temoin infos
       
        nomsTemoin=request.POST.getlist('nomTemoin')
        adressesTemoin=request.POST.getlist('adresseTemoin')
        contacts=request.POST.getlist('contactTemoin')
        print(nomsTemoin)
        for i in range (len(nomsTemoin)):
            t=Temoin(nom=nomsTemoin[i],contact=contacts[i],adresse=adressesTemoin[i],contrat=contrat)
            print(t)
            t.save()
        



        ## save et validator##
        return redirect("/contrats")
    else:
        return render(request,'contrats/create.html')
      


def index(request):
    return render(request,"contrats/index.html")

#view that print client list
def list_contrat(request):
    contrats=Contrat.objects.all()
    return render(request,"contrats/list.html",locals())
#delete client
def delete():
    pass
#update client
def edit_contrat(request,id):
    result=Contrat.objects.filter(pk=id)
    contrat=get_object_or_404(result)
    print(contrat)
    return  render(request,'contrats/edit.html',locals())

def update_contrat(request,id):
     if request.method=='POST':
        #validator
        #client infos
        nom=request.POST.get('nom')
        contact=request.POST.get('contact')
        adress=request.POST.get('adresse')
        date_naiss=request.POST.get('date_naissance')
        #instance
        clt=Client(nom=nom,contact=contact,adresse=adress,date_naissance=date_naiss)
        clt.save()
        ####contrat infos
        montant=request.POST.get('montant')
        duree=request.POST.get('duree')
        date=request.POST.get('date_sgnture')
        #instance
        contrat=Contrat(montant_contrat=montant,date_contrat=date,duree=duree,client=clt)
        contrat.save()
        ###temoin infos
       
        nomsTemoin=request.POST.getlist('nomTemoin')
        adressesTemoin=request.POST.getlist('adresseTemoin')
        contacts=request.POST.getlist('contactTemoin')
        print(nomsTemoin)
        for i in range (len(nomsTemoin)):
            t=Temoin(nom=nomsTemoin[i],contact=contacts[i],adresse=adressesTemoin[i],contrat=contrat)
            print(t)
            t.save()
        
        return HttpResponse("ok")


def detail_contrat(request):
    return render(request,"contrats/detail_contrat.html")