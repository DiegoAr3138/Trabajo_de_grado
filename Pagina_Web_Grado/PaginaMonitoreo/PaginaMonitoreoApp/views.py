from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request): #se va a encargar de registar o  de dar el permiso a la persona
    return render(request, 'login.html')

def home(request):
    return HttpResponse('Home')

def perfil(request):
    return HttpResponse('Perfil')

def señales(request):
    return HttpResponse('Señales')

def dispositivos(request):
    return HttpResponse('Dispositivos')

def antenas(request):   
    return HttpResponse('Antenas')