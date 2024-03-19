from ..models import Versement, Contrat
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse

# formulaire de création d'un client#
def client_form(request):
    return render(request,'clients/create.html')

def create(request):
    return render(request,'clients/create.html')
