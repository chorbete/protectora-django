from django.contrib import admin
from .models import Protectoras, Animales


class AdminAnimales(admin.ModelAdmin):
	list_display = ["__str__","nombre","raza","edad"]
	list_filter = ["nombre","raza","edad"]
	class Meta:
		model = Animales

class AdminProtectoras(admin.ModelAdmin):
	list_display = ["__str__","ubicacion","email"]
	list_filter = ["ubicacion","email"]
	class Meta:
		model = Protectoras

admin.site.register(Protectoras, AdminProtectoras)
admin.site.register(Animales, AdminAnimales)
# Register your models here.
