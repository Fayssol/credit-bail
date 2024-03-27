from django.urls import path
from . import views



app_name = 'askia_admin'


urlpatterns = [
    # affichage des templates
    path('base/', views.base,name='base'),
   

    #transaction
    path('transaction/', views.save_transaction, name="save_transaction"),
    path('transaction_form/', views.transaction_form, name="transaction_form"),

    path('transaction_list',views.transaction_list, name="transaction_list"),
    path('client_list', views.client_liste, name="client_list"),
    path('', views.welcome, name="welcome"),
    path('ajax_transaction_list', views.transaction_list, name="ajax_transaction_list"),
    path('transaction_list/',views.transaction_list, name="transaction_list"),
    
    #contrats
    path('contrat_form/', views.contrat_form,name='contrat_form'),
    path('contrats/', views.list_contrat,name='list_contrat'),
    path('save/', views.save_contrat, name="save_contrat"),
    path('update/<int:id>/', views.update_contrat, name="update_contrat"),
    path('edit/<int:id>/', views.edit_contrat, name="edit_contrat"),



]



