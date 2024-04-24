from django.shortcuts import render,HttpResponse
from .vues.transactions_views import *
from .vues.client_views import *




# Create your views here.


def base(request):
    return render(request,'layouts/base.html')



def welcome(request):
    return render(request, 'pages/index.html')


