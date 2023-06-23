from os import name
from django.db import models
from django.db import migrations ,models

class Band(models.Model):
    name= models.fields.CharField(max_length=100)


class  Users(models.Model):
    Nom=models.CharField(max_length=200)
    Prenom=models.CharField(max_length=300)
    Mot=models.CharField(max_length=50)
    Email=models.EmailField()
    
    class Meta:
        db_table= "Users"