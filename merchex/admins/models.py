from os import name
from django.db import models

class Band(models.Model):
    name= models.fields.CharField(max_length=100)


class  User(models.Model):
    uid=models.CharField(max_length=200)
    uname=models.CharField(max_length=300)
    uemail=models.EmailField(max_length=20)
    
    class Meta:
        db_table= "user"