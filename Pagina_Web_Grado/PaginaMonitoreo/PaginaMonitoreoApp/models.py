from django.db import models

# Create your models here.

class Usuarios(models.Model):
    username = models.CharField(unique=True, max_length=20)# unico y necesario  
    contrasena = models.CharField(max_length=50)# necesario
    nombre = models.CharField(max_length=50) #necesario 
    apellido =  models.CharField(max_length=50) #necesario
    email = models.EmailField(max_length=254)#necesario 
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('NB', 'No Binario'),
        ('T', 'Transgénero'),
        ('O', 'Otro'),
        ('N', 'Prefiero no decirlo'),
    ]
    #de aqui para abajo estas caracteristicas las pueden actualizar despues
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES,null=True, blank=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    telefono = models.CharField(max_length=15,null=True, blank=True)
    direccion = models.CharField(max_length=50,null=True, blank=True)
    OCUPACION_CHOISE = [
        ('E','Estudiante'),
        ('I','Ingeniero'),
        ('O','Otro')
    ]
    ocupacion = models.CharField(max_length=1, choices=OCUPACION_CHOISE, null=True, blank=True)
    create =  models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    fotoperfil = models.ImageField( upload_to='usuarios', height_field=None, width_field=None, max_length=None,null=True, blank=True)

    def __str__(self):
        return 'Nombre: '+self.nombre +' '+self.apellido +'. Correo: '+self.email
    