from django.db import models
from django.contrib.auth.models import AbstractUser






# Create your models here.


class Users(AbstractUser):
    Roles = [
        ('admin', 'administrateur'),
        ('etudiant', 'étudiant'),
        ('prof', 'professeur'),
    ]

    role = models.CharField(
        max_length=25,
        choices=Roles,
        default='prof'
    )

    REQUIRED_FIELDS = ['role', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()} ({self.username})"


class Classe(models.Model):

   nom = models.CharField( max_length=25)



   def  __str__(self):
         return self.nom 

  



class  Matiere(models.Model):

    nom = models.CharField(max_length=25)

    def __str__(self):
      return self.nom



class Etudiant(models.Model):

    user = models.OneToOneField(Users,on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
    age = models.IntegerField()
    matricule = models.CharField(max_length=25)

    def __str__(self):
      return self.user.username



class Professeur(models.Model):

   user = models.OneToOneField(Users,on_delete=models.CASCADE)
   classes= models.ManyToManyField(Classe)
   matiere= models.ForeignKey(Matiere,on_delete=models.CASCADE)

   def __str__(self):
      return self.user.username






class Absence(models.Model):

   choix_de_justification = [

      ('demande_de_repos','repos maladif'),
      ('permission',"permission d'arrêt de cours"),
      ('non_justifie','non_justifie'),
      ('retard_justfie','retard_jstifie')
   ]


  
   etudiant = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
   matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE)
   date  = models.DateField()
   heure = models.TimeField()
   justification = models.CharField(max_length=25,choices=choix_de_justification,default='permission')





   def __str__(self):
      return  f"{self.etudiant}-{self.matiere}-{self.date}"




class Note(models.Model):
   etudiant = models.ForeignKey(Etudiant,on_delete=models.CASCADE)
   matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE)
   valeur = models.DecimalField(max_digits=4,decimal_places=2)

   def __str__(self):
      return f"{self.etudiant} - {self.matiere} : {self.valeur}"