from tabnanny import verbose
from django.db import models

# Create your models here.

class Information(models.Model):
    place= "Bouira" #models.CharField(max_length=50)
    phone_number="+21372343534" #models.CharField(max_length=20)
    email="abdelrahmane.belaidi@esi.dz"#  models.EmailField(max_length=254)

    class Meta:
        verbose_name=("information")
        verbose_name_plural=("informations")

    def __str__(self):
        return self.email
    
