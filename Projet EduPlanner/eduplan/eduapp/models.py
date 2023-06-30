from django.db import models


"""Pour un étudiant en licence 1 de IA """
class Book(models.Model): 
    Jours = models.CharField(max_length=64, null=True ,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 2 de IA """
class Book1(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 3 de IA """
class Book2(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 1 de IM """
class Book3(models.Model): 
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 2 de IM """
class Book4(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 3 de IM """
class Book5(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 1 de GL """
class Book6(models.Model): 
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 2 de GL """
class Book7(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 3 de GL """
class Book8(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 1 de SE&IoT """
class Book9(models.Model): 
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 2 de SE&IoT """
class Book10(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 3 de SE&IoT """
class Book11(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 1 de SI"""
class Book12(models.Model): 
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 2 de SI """
class Book13(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)

"""Pour un étudiant en licence 3 de SI """
class Book14(models.Model):
    Jours = models.CharField(max_length=64, null=True,unique =True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)


class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    matricule=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname

