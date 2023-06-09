from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms


class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
