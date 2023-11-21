from django import forms
from django.contrib.auth.forms import UserCreationForm
from moveApp.models import Utilisateurs


class CustomUserCreationForm(UserCreationForm):
    nomUtil = forms.CharField(required=True)
    preUtil = forms.CharField(required=True)
    nivUtil = forms.ChoiceField(choices=Utilisateurs.NIVEAU_CHOICES, required=True)
    serviceUtil = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Utilisateurs
        fields = UserCreationForm.Meta.fields + ('nomUtil', 'preUtil', 'nivUtil', 'serviceUtil', 'dateCreUtil', 'heureCreUtil', 'derniereOperUtil')
