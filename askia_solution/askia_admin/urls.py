from django.urls import path
from . import views



app_name = 'askia_admin'


urlpatterns = [
    path('base/', views.base,name='base'),
    path('create/', views.create,name='create'),
]



