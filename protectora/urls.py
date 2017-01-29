"""trabajo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *
from . import views

app_name = 'protectora'
urlpatterns = [
#inicio
	url(r'^$', views.inicio, name='inicio'),
#animales
	url(r'^animales', views.verAnimales, name='Ver animales'),
	url(r'^detalles/(?P<animales_id>\d+)', views.detAnimales, name='detalles'),
	url(r'^agregar', views.addAnimal, name='Anadir animal'),
	url(r'^editar/(?P<animales_id>\d+)', views.modAnimal, name='editarAnimal'),
	url(r'^borrarAnimal/(?P<animales_id>\d+)', views.borrarAnimal, name='borrarAnimal'),

#protectoras
	url(r'^protectoras', verProtectora.as_view(), name='Ver protectoras'),
	url(r'^detProt/(?P<pk>\d+)', detProtectoras.as_view(), name='detProt'),
	url(r'^anadirProt', views.addProtectora, name='Anadir protectora'),
	url(r'^editarProt/(?P<protectora_id>\d+)', views.modProtectora, name='editarProtectoral'),
	url(r'^borrarProt/(?P<protectora_id>\d+)', views.borrarProt, name='borrarProt'),

]
