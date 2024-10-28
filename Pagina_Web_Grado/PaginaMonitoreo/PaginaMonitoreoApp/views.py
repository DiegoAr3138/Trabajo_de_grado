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
    return render(request,'perfil.html')

def señales(request):
    return render(request,'señales.html')

def dispositivos(request):
    return render(request,'dispositivos.html')

def antenas(request):   
    return render(request,'antenas.html')