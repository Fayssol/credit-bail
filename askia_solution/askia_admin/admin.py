from django.contrib import admin

from askia_admin.models import Client,Contrat,Versement,Temoin
# # Register your models here.
admin.site.register(Client)
admin.site.register(Temoin)
admin.site.register(Contrat)
admin.site.register(Versement)