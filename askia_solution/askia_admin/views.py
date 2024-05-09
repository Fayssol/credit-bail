from django.shortcuts import render,HttpResponse
from .vues.transactions_views import *
from .vues.client_views import *
from .models import Contrat

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.


def base(request):
    return render(request,'layouts/base.html')


@login_required
def welcome(request):
    en_cours = Contrat.objects.filter(etat="EN_COURS").all().count()
    termines = Contrat.objects.filter(etat="TERMINE").all().count()
    annules = Contrat.objects.filter(etat="ANNULE").all().count()
    redefinis = Contrat.objects.filter(etat="REASSIGNER").all().count()
    return render(request, 'pages/index.html', locals())




def custom_login(request):
    print("je suis la")
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
    else:
        return redirect('/')
    return render(request, 'auth/login.html')

def login_page(request):
     return render(request, "auth/login.html")


def error_404(request, exception):
    return render(request, 'pages/404.html', {})

