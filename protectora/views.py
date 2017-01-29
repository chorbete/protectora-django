from django.shortcuts import  render,get_object_or_404, render_to_response
from .models import Protectoras, Animales
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.urls import reverse 
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import addModelForm, proModelForm, AuthenticationForm
from .models import Animales, Protectoras
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

#Vista Inicio
def inicio(request):
	animales = Animales.objects.all()
	protectora = Protectoras.objects.all()
	context = {
		'animales':animales,
		'protectora':protectora,
	}
	return render(request, 'protectora/inicio.html',context)
	

#Vistas como funciones de Animales
def verAnimales(request):
	animal = Animales.objects.all().order_by('fecha')
	context = {
		'ultimos_animales':animal,	
	}
	return render(request,'protectora/animales.html',context)

def detAnimales (request, animales_id):
	det = Animales.objects.get(pk=animales_id)
	context = {
		'detalles':det,#'variable de la plantilla':dato que definimos arriba
	}
	return render(request, 'protectora/detalles.html',context)

@login_required(login_url='/usuario/ingreso')
def addAnimal(request):
	if request.user.is_authenticated():
		titulo = "Bienvenido %s" %(request.user)
	else:
		titulo= "Bienvenido desconocido"
	form = addModelForm(request.POST or None)
	context = {
		"titulo":titulo,
		"el_form":form,
	}

	if form.is_valid():
		form.save()

		context = {
			"titulo":"Animal agregado correctamente. Muchas gracias %s!" %(request.user),
		}
	return render(request,'protectora/agregar.html',context)

@login_required(login_url='/usuario/ingreso')
def modAnimal(request,animales_id):
	animal = get_object_or_404(Animales, pk=animales_id)
	if request.method =='POST':
		form = addModelForm(request.POST or None, instance=animal)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('protectora:detalles', args=(animales_id,)))
	else:
		form = addModelForm(instance = animal)
	context = {
		'form':form,
	}

	return render(request,'protectora/editarAnimal.html',context)

@login_required(login_url='/usuario/ingreso')
def borrarAnimal(request,animales_id):
	animal = Animales.objects.get(pk=animales_id)
	if request.method == 'POST':
		animal.delete()
		return HttpResponseRedirect('/protectora/animales')
	return render(request,'protectora/borrarAnimal.html',{'animal':animal})
	

#Vistas como clases de Protectora

class verProtectora(ListView):
	model = Protectoras
	template_name = 'protectora/protectora.html'
	

class detProtectoras(DetailView):
	model = Protectoras
	template_name = 'protectora/detProt.html'

@login_required(login_url='/usuario/ingreso')
def addProtectora(request):
	if request.user.is_authenticated():
		titulo = "Bienvenido %s" %(request.user)
	forms = proModelForm(request.POST or None)

	context = {
		"titulo":titulo,
		"form":forms,
	}

	if forms.is_valid():
		forms.save()

		context = {
			"titulo":"Protectora agregada correctamente. Muchas gracias %s!" %(request.user),
		}
	return render(request,'protectora/agregarPro.html',context)

@login_required(login_url='/usuario/ingreso')
def modProtectora(request,protectora_id):
	prot = Protectoras.objects.get(pk=protectora_id)
	if request.method =='POST':
		form = proModelForm(request.POST or None, instance=prot)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('protectora:detProt', args=(protectora_id,)))
	else:
		form = proModelForm(instance = prot)
	context = {
		'form':form,
	}

	return render(request,'protectora/editarProtectora.html',context)


@login_required(login_url='/usuario/ingreso')
def borrarProt(request,protectora_id):
	prot = Protectoras.objects.get(pk=protectora_id)
	if request.method == 'POST':
		prot.delete()
		return HttpResponseRedirect('/protectora/protectoras')
	return render(request,'protectora/borrarProt.html',{'prot':prot})


#def verAnimales(request):
#	ultimos_animales = Animales.objects.order_by('-fecha')[:10]
#	context = {
#		'ultimos_animales':ultimos_animales,	
#	}
#	return render(request,'protectora/animales.html',context)



# Create your views here.
