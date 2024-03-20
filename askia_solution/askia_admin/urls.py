from django.urls import path
from . import views



app_name = 'askia_admin'


urlpatterns = [
    # affichage des templates
    # path('base/', views.base,name='base'),
   

    #les chemins urls
    path('transaction/', views.save_transaction, name="save_transaction"),
    path('create_client/', views.client_form,name='create_client'),
    path('transaction_form/', views.transaction_form, name="transaction_form"),
    path('transaction_list',views.transaction_list, name="transaction_list"),
    path('client_list', views.client_liste, name="client_list"),
    path('', views.welcome, name="welcome"),
]



