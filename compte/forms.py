from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomuserCreationform(UserCreationForm):
    password1 = forms.CharField(
        label="password",
        strip="False",
        widget= forms.PasswordInput(attrs={'autocomplete':'new-password}'}),
        
    )
    password2 = forms.CharField(
        label="password confirmation",
        widget= forms.PasswordInput(attrs={'autocomplete':'new-passeword'}),
        strip=False,
    )



class Meta(UserCreationForm):
    fields = UserCreationForm.Meta.fields + ("password1","password2")