from django.conf.urls import url, include
from . import views

app_name = 'usuario'
urlpatterns = [

	url(r'^registro$', views.nuevo_usuario, name='nuevo_usuario'), #Url de registro del Usuario
	url(r'^ingreso$', views.ingresar, name='ingresar'), # Url de login del Usuario
	url(r'^cerrarsesion$', views.cerrarSesion, name='cerrar'), # Url para el cierre de sesion
]
