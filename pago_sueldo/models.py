from django.db import models
from usuarios.models import UsuarioPersonalizado
from django.core.validators import MinValueValidator

# Create your models here.

class CargaHoraria(models.Model):
    cantidad = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    empleado = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete=models.CASCADE,
        null=True,
        related_name='cargas_horarias'
    )
    usuario_activo = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete=models.CASCADE,
        null=True,
        related_name='cargas_horarias_creadas'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)


class SueldoHora(models.Model):
    valor = models.IntegerField(null=True, blank=True)
    empleado = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete=models.CASCADE,
        null=True,
        related_name='sueldos_hora'
    )
    usuario_activo = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete=models.CASCADE,
        null=True,
        related_name='sueldos_hora_creados'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)