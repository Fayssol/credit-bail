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



# import hashlib
# import base64
# from django.urls import reverse

# def hash_id(id):
#     # Convertir l'ID en une chaîne de caractères
#     id_str = str(id)
    
#     # Générer un hash à partir de l'ID
#     hashed_id = hashlib.sha256(id_str.encode()).digest()
    
#     # Encoder le hash en base64
#     encoded_id = base64.urlsafe_b64encode(hashed_id).decode().rstrip("=")
    
#     return encoded_id

# def unhash_id(encoded_id):
#     # Décoder l'ID depuis base64
#     decoded_id = base64.urlsafe_b64decode(encoded_id + "==").decode()
#     return int(decoded_id)

# # Exemple d'utilisation
# id = 123
# encoded_id = hash_id(id)
# print("ID encodé:", encoded_id)

# decoded_id = unhash_id(encoded_id)
# print("ID décodé:", decoded_id)

# # Utilisation dans les URLs Django
# hashed_id = hash_id(123)
# url = reverse('detail', kwargs={'hashed_id': hashed_id})
# print("URL:", url)


# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('detail/<str:hashed_id>/', views.detail, name='detail'),
# ]


# # views.py
# from django.shortcuts import get_object_or_404
# from .models import VotreModele

# def detail(request, hashed_id):
#     id = unhash_id(hashed_id)
#     obj = get_object_or_404(VotreModele, id=id)
#     # Faire ce que vous voulez avec l'objet
