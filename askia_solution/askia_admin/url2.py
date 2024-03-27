from django.urls import path
from . import views



app_name = 'askia_admin'


urlpatterns = [
   
    #contrats
    path('contrat_form/', views.contrat_form,name='contrat_form'),
    path('contrats/', views.list_contrat,name='list_contrat'),
    path('save/', views.save_contrat, name="save_contrat"),
    path('update/<int:id>/', views.update_contrat, name="update_contrat"),
    path('edit/<int:id>/', views.edit_contrat, name="edit_contrat"),


]



