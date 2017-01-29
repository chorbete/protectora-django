from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from usuario.models import Usuario

# Formulario para el registro de un Cliente
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
