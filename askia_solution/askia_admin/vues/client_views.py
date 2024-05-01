from ..models import Versement,Client,Temoin,Contrat
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from datetime import date
from django.http import JsonResponse
from django.urls import reverse
from ..models import Versement, Contrat,Client
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

from datetime import date

from django.shortcuts import render



# formulaire de création d'un contrat#
def contrat_form(request):
    date_actuelle = date.today().isoformat()
    return render(request,'contrats/create.html', locals())

# def client_liste(request):
#     return render(request,'clients/liste.html')


def save_contrat(request):

    if request.method=='POST':
        #validator
        #client infos
        print("POST")
        nom=request.POST.get('nom')
        contact=request.POST.get('contact')
        adress=request.POST.get('adresse')
        date_naiss=request.POST.get('date_naissance')
        #instance
        clt=Client(nom=nom,contact=contact,adresse=adress,date_naissance=date_naiss)
        clt.save()
        ####contrat infos
        montant=request.POST.get('montantC')
        duree=request.POST.get('duree')
        date=request.POST.get('date_sgnture')

        if request.path == "/reassigner/":
            id_contrat = int(request.POST.get('contrat_parent'))
            parent_contrat = Contrat.objects.get(pk=id_contrat)
            contrat=Contrat(montant_contrat=montant,date_contrat=date,duree=duree,client=clt)
            contrat.contrat_parent = parent_contrat
            parent_contrat.etat = "REASSIGNER"
            parent_contrat.save()
        else:    
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
      


# def index(request):
#     date_actuelle = date.today().isoformat()

#     return render(request,"contrats/index.html", locals())

#view that print client list
def list_contrat(request):

   
    return render(request,"contrats/list.html")
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


def detail_contrat(request,id):
    date_actuelle = date.today().isoformat()
    contrat=Contrat.objects.get(pk=id)
    if contrat.versement_set.all().last() is not None:
        reste = contrat.montant_contrat - contrat.versement_set.all().last().montant_total_paye
        boolle = True
    else:
        reste = contrat.montant_contrat 
        boolle = False    
    return render(request,"contrats/detail_contrat.html",{"contrat":contrat, "reste":reste, "boolle":boolle, "date_actuelle":date_actuelle})

@csrf_protect
def contrat_view(request):
    if request.method == "POST":
        draw = int(request.POST.get('draw'))
        start = int(request.POST.get('start'))
        length = int(request.POST.get('length'))
        search = request.POST.get('search[value]')
        date_from = request.POST.get('from_date', None)
        date_to = request.POST.get('to_date', None)
        
        filtered_contrat = Contrat.objects.order_by('-date_contrat', '-id')

        # filtered_contrat = Contrat.objects.exclude(etat="REASSIGNER").order_by('-date_contrat', '-id')

        if search :
            filtered_contrat = filtered_contrat.filter(
                Q(montant_contrat__icontains=search)|
                Q(duree__icontains=search)|
                Q(date_contrat__icontains=search)|
                Q(client__nom__icontains=search)|
                Q(status__icontains=search)|
                Q(etat__icontains=search)
                
            )
        ##recherche entre deux dates
        if date_from and date_to:
            filtered_contrat=filtered_contrat.filter(
                date_contrat__range=[date_from, date_to]
                
            )
        #nbre total d'objets 
        total_records=Contrat.objects.count()
        ##nbre total d'objets filtrés
        total_filtered_records=filtered_contrat.count()
        
        data={
             "draw": draw,
            "recordsTotal": total_records,
            "recordsFiltered": total_filtered_records,
            "data":[{
                "id":contrat.id,
                "date_contrat":contrat.date_contrat,
                "montant_contrat":'{:,.0f}'.format(contrat.montant_contrat).replace(',',' '),
                "duree":contrat.duree,
                "client":contrat.client.nom,
                "status":contrat.status,
                "etat":contrat.etat,
                
                
                
            } for contrat in filtered_contrat[start:start+length]
            ],
        }
        return JsonResponse(data)
    return render(request,'contrats/list.html')
        
            

def annuler_contrat(request):
    if request.method == "POST":
        canceled_id = int(request.POST.get('canceled_id'))
        # print(canceled_id)
        contrat = Contrat.objects.get(pk=canceled_id)
        contrat.etat = "ANNULE"
        contrat.save()
        return redirect('/contrats')
        # return render(request,'contrats/list.html')