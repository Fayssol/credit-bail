from django.shortcuts import render,HttpResponse

# Create your views here.


def base(request):
    return render(request,'layouts/base.html')

def create(request):
    return render(request,'clients/create.html')

def index(request):
    return HttpResponse("Welcome")

