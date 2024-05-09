from . import views

from django.urls import path




app_name = 'askia_admin'




urlpatterns = [
    # affichage des templates
    path('base/', views.base,name='base'),
   


    #transaction
    path('transaction/', views.save_transaction, name="save_transaction"),
    path('transaction_form/', views.transaction_form, name="transaction_form"),
    path('transaction_index',views.transaction_index, name="transaction_index"),
    
    path('ajax_transaction_list', views.transaction_list, name="ajax_transaction_list"),
    path('ajax_transaction_list_contrat/', views.transaction_list, name="ajax_transaction_list_contrat"),

    path('transaction_modal/',views.save_transaction, name="transaction_modal"),
    
    #contrats
    path('contrat_form/', views.contrat_form,name='contrat_form'),
    path('contrats/', views.list_contrat,name='list_contrat'),
    path('contrats_pdf/', views.contrat_list_pdf,name='contrat_list_pdf'),
    path('contrat_pdf/', views.contrat_def_pdf, name="contrat_def_pdf"),
    path('save/', views.save_contrat, name="save_contrat"),
    path('update/<int:id>/', views.update_contrat, name="update_contrat"),  
    path('edit/<int:id>/', views.edit_contrat, name="edit_contrat"),
    path('detail_contrat/<int:id>/', views.detail_contrat,name='detail_contrat'),

    path('ajax_contrat_list', views.contrat_view, name="ajax_contrat_list"),
    path('annuler_contrat', views.annuler_contrat, name="annuler_contrat"),

     path('reassigner/', views.save_contrat, name="reassigner_contrat"),

    path('home/', views.welcome, name="welcome"),
    path('login/', views.custom_login, name='login_verify'),
    path('', views.login_page, name='login_page'),

     path('logout/', views.logout_view, name='logout'),

]



