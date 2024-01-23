from django.urls import path
from . import views
<<<<<<< HEAD


app_name = 'askia_admin'


urlpatterns = [
    path('base/', views.base,name='base'),
    path('create/', views.create,name='create'),
]
=======
urlpatterns = [
    path("",views.index , name="")
]
>>>>>>> a3e5a3f6f06ef1471565c781c80f9cbdcdb5a1b0
