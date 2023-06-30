from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventForm

def index(request):
    eventos = Evento.objects.get().order_by('fecha')
    contexto = {
        'eventos' : eventos
    }
    return render(request, './agenda/index.html', contexto)

def crear(request):
    if (request.method == 'GET'):
        formulario = EventForm
        contexto = {
            'formulario' : formulario
        }
        return render(request, './agenda/crear.html', contexto)
    
    if (request.method == 'POST'):
        eventos = Evento.objects.filter(nombre__contains=request.GET.get('buscar', ''))
        contexto = {
            'eventos' : eventos
        }
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('agenda')

def detalles(request, id):
    evento = Evento.objects.get(id=id)
    contexto = {
        'evento' : evento
    }
    return render(request, './agenda/detalles.html', contexto)

def editar(request, id):
    evento = Evento.objects.get(id=id)
    if (request.method == 'GET'):
        formulario = EventForm(instance=evento)
        contexto = {
            'evento' : evento,
            'formulario' : formulario,
            'id' : id
        }
        return render(request, './agenda/editar.html', contexto)
    
    if (request.method == 'POST'):
        form = EventForm(request.POST, instance=evento)
        if form.is_valid:
            form.save()
        return redirect('detalles_evento', id=id)

def borrar(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('agenda')