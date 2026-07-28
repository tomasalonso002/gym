from django.db import models
from django.contrib.auth.models import User
from usuarios.models import UsuarioPersonalizado



class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to='rutinas/',null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
class RutinaPersonalizada(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to='rutinas/',null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='rutinas_personalizadas' )
    def __str__(self):
        return self.nombre