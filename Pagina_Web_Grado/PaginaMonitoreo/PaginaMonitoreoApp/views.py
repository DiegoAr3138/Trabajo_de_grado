from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib import messages

# Create your views here.
def login(request): #se va a encargar de registar o  de dar el permiso a la persona
    return render(request, 'login.html')


def sing_up(request):
    return HttpResponse('cargo')



# esto por el momento no nos interesa
def home(request):
    return render(request, 'home.html')

def perfil(request):
    return HttpResponse('Perfil')

def señales(request):
    return HttpResponse('Señales')

def dispositivos(request):
    return HttpResponse('Dispositivos')

def antenas(request):   
    return HttpResponse('Antenas')