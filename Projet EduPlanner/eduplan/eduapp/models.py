from django.db import models


class Licence1IA(models.Model): 
    id = models.IntegerField(unique=True,primary_key=True)
    Jours = models.CharField(max_length=64, unique=True)
    # Matières = models.CharField(max_length=64, null=True)
    # Heures = models.CharField(max_length=64, null=True)

