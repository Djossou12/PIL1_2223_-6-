from django.db import models


"""Pour un étudiant en licence 1 de IA """
class IA_1(models.Model): 
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)

"""Pour un étudiant en licence 2 de IA """
class IA_2(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


"""Pour un étudiant en licence 3 de IA """
class IA_3(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


"""Pour un étudiant en licence 1 de IM """
class IM_1(models.Model): 
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


"""Pour un étudiant en licence 2 de IM """
class IM_2(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.TimeField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)



"""Pour un étudiant en licence 3 de IM """
class IM_3(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)

"""Pour un étudiant en licence 1 de GL """

class GL_1(models.Model): 
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)

"""Pour un étudiant en licence 2 de GL """
class GL_2(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)

"""Pour un étudiant en licence 3 de GL """
class GL_3(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


"""Pour un étudiant en licence 1 de SE&IoT """
class SEIOT_1(models.Model): 
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


"""Pour un étudiant en licence 2 de SE&IoT """
class SEIOT_2(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


"""Pour un étudiant en licence 3 de SE&IoT """
class SEIOT_3(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


"""Pour un étudiant en licence 1 de SI"""
class SI_1(models.Model): 
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)

"""Pour un étudiant en licence 2 de SI """
class SI_2(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)

"""Pour un étudiant en licence 3 de SI """
class SI_3(models.Model):
    Jours = models.CharField(max_length=64, null=True)
    Matières = models.CharField(max_length=64, null=True)
    Heures = models.CharField(max_length=64, null=True)
    Professeur = models.CharField(max_length=64, null=True)
    Groupe = models.IntegerField(default=1)


class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    matricule=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname

