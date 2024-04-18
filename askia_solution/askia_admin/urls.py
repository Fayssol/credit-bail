from django.urls import path
from . import views



app_name = 'askia_admin'


urlpatterns = [
    # affichage des templates
    path('base/', views.base,name='base'),
   

    #transaction
    path('transaction/', views.save_transaction, name="save_transaction"),
    path('transaction_form/', views.transaction_form, name="transaction_form"),
    path('transaction_index',views.transaction_index, name="transaction_index"),
    path('', views.welcome, name="welcome"),
    path('ajax_transaction_list', views.transaction_list, name="ajax_transaction_list"),
    path('transaction_modal/',views.save_transaction, name="transaction_modal"),
    
    #contrats
    path('contrat_form/', views.contrat_form,name='contrat_form'),
    path('contrats/', views.list_contrat,name='list_contrat'),
    path('save/', views.save_contrat, name="save_contrat"),
    path('update/<int:id>/', views.update_contrat, name="update_contrat"),  
    path('edit/<int:id>/', views.edit_contrat, name="edit_contrat"),
    path('detail_contrat/', views.detail_contrat,name='detail_contrat'),
<<<<<<< HEAD
=======
    path('ajax_contrat_list', views.contrat_view, name="ajax_contrat_list"),
>>>>>>> d7d61d8a029cdcdaf8117131ad5c9ed75330f9e2


]



