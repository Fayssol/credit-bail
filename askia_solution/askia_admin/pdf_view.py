from django.shortcuts import redirect
from os.path import dirname, abspath
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
from .templating_latex.controlleur import generate_pdf as generer




    
    

def get_pdf_from_http(request,model, context, pdf_type):
    success_message = None
    error_message = None
    try:
        templae_dir = model+"/"+pdf_type+"/"
        pdf_name = pdf_type +".pdf" 
        generer(context, pdf_name,templae_dir)        
        success_message = 'Suxxes !!!'
        messages.success(request, success_message)     
      
        with open( dirname(abspath(__file__))+ "/jinja_template/out/menageOut.pdf", "rb") as my_file:
            return HttpResponse(my_file.read(), content_type = "application/pdf")
    except Exception as e:
        error_message = f"Une erreur s'est produite : {str(e)}"
        messages.error(request, error_message)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    

   

    
