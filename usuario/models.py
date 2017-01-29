from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
	nombre_usuario = models.CharField(max_length=10)
	usuario = models.ForeignKey(User,blank=True)
	
	def __str__(self):
		return self.nombre_usuario

# Create your models here.
