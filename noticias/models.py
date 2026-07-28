from django.db import models
from usuarios.models import UsuarioPersonalizado
# Create your models here.

class Noticias(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    contenido = models.CharField(max_length=500, null=True, blank=True)
    archivo = models.ImageField(upload_to='noticias/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='noticias' )
    def __str__(self):
        return self.titulo