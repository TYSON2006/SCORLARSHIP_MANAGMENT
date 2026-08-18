from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Classe, Matiere, Etudiant, Professeur, Absence

# Register your models here.


admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Etudiant)
admin.site.register(Professeur)
admin.site.register(Absence)


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("role",)}),)


admin.site.register(Users, CustomUserAdmin)
