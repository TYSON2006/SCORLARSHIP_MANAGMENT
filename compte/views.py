from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

    return render(request, "connexion.html")


@login_required
def acceuil(request):
    return render(request, "acceuil.html")





def deconnexion_view(request):
    logout (request)
    return redirect('connexion')




def acceuil_view(request):

    if request.user.role == 'prof':
        return render(request,'compte/dashboard_prof.html')
    elif request.user.role == 'etudiant':
        return render(request,'compte/dashborad_etudiant.html')
    else:
        return render(request,'compte/acceuil.html')




