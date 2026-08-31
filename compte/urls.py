from django.urls import path
from. import views



urlpatterns = [
        path("connexion/", views.connect_view ,name="connexion"),
        path("acceuil/",views.acceuil,name="acceuil"),
        path("deconnexion/",views.deconnexion_view,name="deconnexion"),
        path("",views.connect_view,name="home"),
        path("liste-etudiants/",views.liste_etudiants,name="liste_etudiants"),
        path("ajouter_etudiant/",views.ajouter_etudiant, name="ajouter_etudiant"),
        path("liste_professeurs/",views.liste_professeurs, name="liste_professeurs"),
        path("ajouter_professeurs/",views.ajouter_professeurs,name='ajouter_professeurs'),
        path("supprimer_etudiant/<int:etudiant_id>/", views.supprimer_etudiant, name="supprimer_etudiant"),
        path("modifier_etudiant/<int:etudiant_id>/", views.modifier_etudiant, name="modifier_etudiant"),
        path("supprimer_professeur/<int:professeur_id>",views.supprimer_professeur,name="supprimer_professeur"),
        path("modifier_professeur/<int:professeur_id>",views.modifier_professeur,name="modifier_professeur"),
        path("ajouter_note/",views.ajouter_note,name="ajouter_note"),
        path("dashboard_prof/",views.dashboard_prof,name="dashboard_prof"),
        path("dashboard_etudiant/",views.dashboard_etudiant,name="dashboard_etudiant"),
        path("mes_classes/",views.mes_classes,name="mes_classes")
       
]
