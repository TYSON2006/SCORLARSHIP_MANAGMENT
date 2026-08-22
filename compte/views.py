from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Etudiant 
from .models import Professeur

# Create your views here.


def connect_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("acceuil")
        else:
            messages.error(request, "Nom d'utilisateur ou password incorrect.")

    return render(request, "compte/connexion.html")


@login_required
def acceuil(request):
    return render(request, "compte/acceuil.html")





def deconnexion_view(request):
    logout (request)
    return redirect('connexion')




def acceuil_view(request):

    if request.user.role == 'admin':
        return render(request,'compte/acceuil.html')
    
    elif request.user.role == 'etudiant':
        return render(request,'compte/dashboard_etudiant.html')

    elif request.user.role == 'prof':
        return render(request,'compte/dashboard_prof.html')
   




@login_required
def  liste_etudiants(request):
    etudiants =  Etudiant.objects.all()
    return render(request,'compte/liste_etudiants.html',{'etudiants':etudiants})





@login_required
def ajouter_etudiant(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        classe_id = request.POST["classe_id"]
        age = request.POST["age"]
        matricule = request.POST["matricule"] 
        if Users.objects.filter(username=username).exists():

            messages.error(request,"Ce nom d'tulilisateur est déjà utilisé")
            return render(request,"compte/ajouter_etudiant.html")
        nouvelle_utilisateur = Users.objects.create_user(username=username,password=password,role='etudiant')
        classe_obj= Classe.objects.get(id = classe_id)
        Etudiant.objects.create (user= nouvelle_utilisateur, classe=classe_obj,age=age,matricule=matricule)
        return redirect('liste_etudiants')
    return render(request,'compte/ajouter_etudiant.html')
        
        
        


def liste_professeurs(request):
    professeurs = Professeur.objects.all()
    context={
        "professeurs":professeurs
    }
    
    return render(request,'compte/liste_professeurs.html',context)

        
   


 
def ajouter_professeurs(request):
    if request.method == 'POST':
        username = request.POST ["username"]
        password = request.POST ["password"]
        matiere_id = request.POST["matiere_id"]
        classes_ids = request.POST.getlist("classes_ids")
        if Users.objects.filter(username=username).exists():
            messages.error(request,"ce nom est déjà utilisé")
            return render(request,"compte/ajouter_professeurs.html")
        nouvelle_utilisateur = Users.objects.create_user(username=username,password=password,role='prof')
        nouveau_prof = Professeur.objects.create(user=nouvelle_utilisateur,matiere=matiere_obj)
        nouveau_prof.classes.set("classes_ids")
        return render("liste_professeurs")

    return render(request,"compte/ajouter_professeurs.html")


@login_required
def supprimer_etudiant(request,etudiant_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    etudiant.delete()
    return redirect('liste_etudiants')



@login_required
def modifier_etudiant(request, etudiant_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)

    if request.method == 'POST':
        etudiant.age = request.POST["age"]
        etudiant.matricule = request.POST["matricule"]
        classe_obj = Classe.objects.get(id=request.POST["classe"])
        etudiant.classe = classe_obj
        etudiant.save()

        etudiant.user.username = request.POST["username"]
        etudiant.user.save()

        return redirect('liste_etudiants')

    return render(request, 'compte/modifier_etudiant.html', {'etudiant': etudiant})