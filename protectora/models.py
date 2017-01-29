from __future__ import unicode_literals

from django.db import models

class Protectoras(models.Model):
	nombre = models.CharField(max_length=50)
	ubicacion = models.CharField(max_length=50)
	descripcion = models.TextField()
	email = models.EmailField()
	fecha_ingreso = models.DateField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return self.nombre
	

class Animales(models.Model):
	protectora = models.ForeignKey(Protectoras,on_delete=models.CASCADE)
	perro = 'Perro'
	gato = 'Gato'
	exotico = 'Exotico'
	tipo_eleccion = (
		(perro,'Perro'),
		(gato,'Gato'),
		(exotico,'Exotico'),
	)
	tipo = models.CharField(max_length=10,choices=tipo_eleccion,default=perro)
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	edad = models.IntegerField(default=0)
	fecha = models.DateField(auto_now_add=True,auto_now=False)
	descripcion = models.TextField()
	def __str__(self):
		return self.tipo


