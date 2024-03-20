
from django.db import models

# Create your models here.
class Personne(models.Model):
    nom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    date_naissance=models.DateField()
    contact=models.CharField(max_length=15)
    
    def __str__(self):
        return self.nom + " " + self.adresse + " " + self.contact
    
    class Meta:
        abstract = True
        
class Client(Personne):
    pass


class Contrat(models.Model):
    id = models.BigAutoField(primary_key=True)
    contrat_parent= models.OneToOneField("self", on_delete=models.PROTECT, null=True,blank=True, related_name="contrats_enfants")
    montant_contrat=models.IntegerField()
    duree=models.CharField(max_length=50)  

    Etat = models.TextChoices("Etat", "EN_COURS ANNULE TERMINE")

    etat = models.CharField(max_length=10, choices=Etat.choices, default=Etat.EN_COURS)

    Status = models.TextChoices("Status", "A_JOUR EN_RETARD")

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.A_JOUR)
    date_contrat=models.DateField()
    client=models.OneToOneField(Client,on_delete=models.CASCADE,null=True)
    
    
class Temoin(Personne):
    contrat=models.ForeignKey(Contrat,on_delete=models.CASCADE)
    

class Versement(models.Model):
    montant_versement = models.IntegerField()
    date_versement = models.DateField()
    montant_total_paye = models.IntegerField(default=0) 
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    note = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Calculer le nouveau montant total payé en ajoutant le montant du versement actuel
        # au montant total payé précédent dans le versement
        self.montant_total_paye += self.montant_versement
        super().save(*args, **kwargs)  # Appeler la méthode save() du modèle parent



    
    
class Vaque(models.Model):
    date_arrivee=models.DateField()
    nbre_moto=models.IntegerField()
    montant_total=models.IntegerField()
    
    
