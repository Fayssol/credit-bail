from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .vues.transactions_views import *
from .vues.client_views import *
from .models import Contrat, Versement

# Create your views here.


def base(request):
    return render(request,'layouts/base.html')


def index(request):
    return HttpResponse("Welcome")




