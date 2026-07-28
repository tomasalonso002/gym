from django.db import models

# Create your models here.

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    dias_por_semana = models.IntegerField()
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Cuota(models.Model):
    usuario = models.ForeignKey('usuarios.UsuarioPersonalizado', on_delete=models.CASCADE,related_name='cuotas')
    plan =models.ForeignKey(Plan, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'),('pagada', 'Pagada')], default='pendiente')
    activo = models.BooleanField(default=True)


class Pago(models.Model):
    cuota = models.ForeignKey(Cuota, on_delete=models.CASCADE, related_name='pagos')
    metodo = models.CharField(max_length=20,choices=[('efectivo', 'Efectivo'),('transferencia', 'Transferencia')])
    comprobante = models.ImageField(upload_to='comprobantes/',null=True,blank=True)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('pendiente_revision', 'Pendiente revisión'),('aprobado', 'Aprobado'),('rechazado', 'Rechazado')])
    activo = models.BooleanField(default=True)
    