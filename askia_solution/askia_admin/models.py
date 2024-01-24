
from django.db import models

# Create your models here.
class Personne(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    date_naissance=models.DateField(auto_now_add=True)
    contact=models.CharField(max_length=15)
    
    def __str__(self):
        return self.nom + " " + self.prenom + " " + self.date_naissance + " " + self.contact
    
    class Meta:
        abstract = True
        
class Client(Personne):
    pass


class Contrat(models.Model):
    id = models.BigAutoField(primary_key=True,default=0)
    parent= models.OneToOneField("self", on_delete=models.PROTECT, null=True, blank=True, related_name="contrats")
    montant_contrat=models.IntegerField()
    duree=models.IntegerField()    
    etat=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    date_contrat=models.DateField()
    fichier=models.CharField(max_length=50)
    client=models.OneToOneField(Client,on_delete=models.CASCADE,null=True)
    
    
class Temoin(Personne):
    contrat=models.ForeignKey(Contrat,on_delete=models.CASCADE,default=0)
    
    
        
class Versement(models.Model):
    montant_versement=models.IntegerField()
    date_versement=models.DateField()
    montant_total_paye=models.IntegerField()
    contrat=models.ForeignKey(Contrat, on_delete=models.CASCADE,default=0)
    
    
class Vaque(models.Model):
    date_arrivee=models.DateField()
    nbre_moto=models.IntegerField()
    montant_total=models.IntegerField()
    
    
