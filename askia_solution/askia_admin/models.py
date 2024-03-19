import uuid
from django.db import models

# Create your models here.
class Personne(models.Model):
    nom=models.CharField(max_length=50)
    # prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    date_naissance=models.DateField()
    contact=models.CharField(max_length=15)
    
    def __str__(self):
        return self.nom + " " + self.prenom + " " + self.adresse + " " + self.contact
    
    class Meta:
        abstract = True
        
class Client(Personne):
    pass


class Contrat(models.Model):
    contrat_parent= models.ForeignKey("self", on_delete=models.CASCADE, null=True,blank=True, related_name="contrats_enfants")
    montant_contrat=models.IntegerField()
    duree=models.CharField(max_length=50)  

    Etat = models.TextChoices("Etat", "EN_COURS ANNULE TERMINE")

    etat = models.CharField(max_length=10, choices=Etat.choices, default=Etat.EN_COURS)

    Status = models.TextChoices("Status", "A_JOUR EN_RETARD")

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.A_JOUR)
    date_contrat=models.DateField()
    fichier=models.FileField(max_length=50)
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
    
    
