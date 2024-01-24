from django.shortcuts import render,HttpResponse

# Create your views here.


def base(request):
    return render(request,'layouts/base.html')

def create(request):
    return render(request,'clients/create.html')

def index(request):
    return HttpResponse("Welcome")
<<<<<<< HEAD

=======
>>>>>>> fccce1c256e78506f7fb7c5e7c6dacc9dc08b7eb
