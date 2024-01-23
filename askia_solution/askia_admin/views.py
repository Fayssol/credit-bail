from django.shortcuts import render,HttpResponse

# Create your views here.
<<<<<<< HEAD

def base(request):
    return render(request,'layouts/base.html')

def create(request):
    return render(request,'clients/create.html')
=======
def index(request):
    return HttpResponse("Welcome")
>>>>>>> a3e5a3f6f06ef1471565c781c80f9cbdcdb5a1b0
