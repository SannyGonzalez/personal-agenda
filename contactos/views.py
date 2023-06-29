from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactForm

##########################################################################################################################

#Esta es la vista del indice, con la logica del buscador
def index(request):
    contactos = Contacto.objects.filter(nombre__contains=request.GET.get('buscar', ''))
    contexto = {
        'contactos' : contactos
    }
    return render(request, './contactos/index.html', contexto)

#Esta es la vista de la creacion de contactos, en un apartado esta el codigo para los metodos GET que renderiza el html necesario y para los POST que crean el nuevo registro en la base de datos y redirecciona al index
def crear(request):
    if (request.method == 'GET'):
        formulario = ContactForm
        contexto = {
            'formulario' : formulario
        }
        return render(request, './contactos/crear.html', contexto)
    
    if (request.method == 'POST'):
        contactos = Contacto.objects.filter(nombre__contains=request.GET.get('buscar', ''))
        contexto = {
            'contactos' : contactos
        }
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('contactos')

##########################################################################################################################

#Vista para los detalles de los contactos, renderiza el html necesario y lleva el contexto de la lista de registros
def detalles(request, id):
    contacto = Contacto.objects.get(id = id)
    contexto = {
        'contacto' : contacto
    }
    return render(request, './contactos/detalles.html', contexto)

##########################################################################################################################

#Vista para editar el contacto, renderiza un html si es metodo GET y redirecciona a los detalles cuando el metodo es GET
def editar(request, id):
    contacto = Contacto.objects.get(id=id)
    if (request.method == 'GET'):
        formulario = ContactForm(instance=contacto)
        contexto = {
            'contacto' : contacto,
            'formulario' : formulario,
            'id' : id
        }
        return render(request, './contactos/editar.html', contexto)
    
    if (request.method == 'POST'):
        form = ContactForm(request.POST, instance=contacto)
        if form.is_valid:
            form.save()
        return redirect('detalles_contacto', id=id)

##########################################################################################################################

#Vista para borrar un registro de la base de datos, al hacerse se redirecciona al index
def borrar(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()
    return redirect('contactos')