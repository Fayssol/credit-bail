from django.shortcuts import render,HttpResponse
from .vues.transactions_views import *
from .vues.client_views import *
from .models import Contrat



# Create your views here.


def base(request):
    return render(request,'layouts/base.html')



def welcome(request):
    en_cours = Contrat.objects.filter(etat="EN_COURS").all().count()
    termines = Contrat.objects.filter(etat="TERMINE").all().count()
    annules = Contrat.objects.filter(etat="ANNULE").all().count()
    redefinis = Contrat.objects.filter(etat="REASSIGNER").all().count()
    return render(request, 'pages/index.html', locals())


