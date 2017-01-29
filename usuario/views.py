from django.shortcuts import render

from django.shortcuts import render, render_to_response, loader, HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from usuario.models import Usuario

# View que permite el registro de un nuevo usuario
def nuevo_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = request.POST['username']
            user = User.objects.get(username=usuario)
            cliente = Usuario.objects.create(nombre_usuario=usuario, usuario=user)
            cliente.save()
            return HttpResponseRedirect('/protectora')
    else:
        form = UserCreationForm()
    template = loader.get_template('usuario/registro.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# View que permite el login de un cliente
def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                login(request, acceso)
                return HttpResponseRedirect('/protectora')
            else:
                return render(request,'usuario/incorrecto.html')
    else:
        form = AuthenticationForm()
    template = loader.get_template('usuario/login.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# View que permite el logout de un cliente, vista solo permitida para clientes ya logueados
@login_required(login_url='/ingreso')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect('/protectora')


# Create your views here.
