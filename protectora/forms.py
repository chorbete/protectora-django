from django import forms
from django.forms import ModelForm
from .models import Animales, Protectoras
from django.contrib.auth.models import User

class addModelForm(forms.ModelForm):
	class Meta:
		model = Animales
		fields =('protectora','tipo','nombre','raza','color','edad','descripcion')

class proModelForm(forms.ModelForm):
	class Meta:
		model = Protectoras
		fields =('nombre','ubicacion','descripcion','email')

class AuthenticationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
