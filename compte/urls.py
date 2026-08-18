from django.urls import path
from. import views



urlpatterns = [
    path("connexion/", views.connect_view ,name="connexion"),
    path("acceuil/",views.acceuil,name="acceuil"),
    path("deconnexion/",views.deconnexion_view,name="deconnexion"),
    path("",views.connect_view,name="home"),
    path("liste-etudiants/",views.liste_etudiants,name="liste_etudiants"),
    path("ajouter_etudiant/",views.ajouter_etudiant, name="ajouter_etudiants"),
    path("liste_professeurs/",views.liste_professeurs, name="liste_professeurs")
]
