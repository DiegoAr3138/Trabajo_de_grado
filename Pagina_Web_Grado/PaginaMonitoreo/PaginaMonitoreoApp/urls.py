from django.urls import path, include 
from PaginaMonitoreoApp import views

urlpatterns = [
    path('',views.login,name='Login'),
    path('home/',views.home,name='Home'),
    path('perfil/',views.perfil,name='Perfil'),
    path('señales/',views.señales,name='Señales'),
    path('dispositivos/',views.dispositivos ,name='Dispositivos'),
    path('antenas/',views.antenas,name='Antenas'),
]