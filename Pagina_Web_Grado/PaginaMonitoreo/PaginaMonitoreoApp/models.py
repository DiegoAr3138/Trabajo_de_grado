from django.db import models

# Create your models here.

class Usuarios(models.Model):
    username = models.CharField(unique=True, max_length=20)
    contrasena = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido =  models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('NB', 'No Binario'),
        ('T', 'Transgénero'),
        ('O', 'Otro'),
        ('N', 'Prefiero no decirlo'),
    ]
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    OCUPACION_CHOISE = [
        ('E','Estudiante'),
        ('I','Ingeniero'),
        ('O','Otro')
    ]
    ocupacion = models.CharField(max_length=1, choices=OCUPACION_CHOISE)
    create =  models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    fotoperfil = models.ImageField( upload_to='usuarios', height_field=None, width_field=None, max_length=None)