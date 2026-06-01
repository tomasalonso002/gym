from django.db import models

from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=20, null=True, blank=True)
    dni = models.CharField(max_length=8, null= True, blank=True)
    foto_perfil = models.ImageField(upload_to='users_fp', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rol_usuario = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, default=2)
    def __str__(self):
        return f"{self.username} - {self.dni}"
