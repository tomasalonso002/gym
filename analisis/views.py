from django.shortcuts import render
from django.utils import timezone
from cuotas.models import Pago
from usuarios.models import UsuarioPersonalizado
from collections import defaultdict
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('cuotas.add_pago')
def analisis(request):
    usuarios_activos = UsuarioPersonalizado.objects.filter(
        is_active=True,
        groups__id = 2
    ).count()

    hoy = timezone.now().date()

    usuarios_deudores = UsuarioPersonalizado.objects.filter(
        cuotas__fecha_vencimiento__lt=hoy,
        cuotas__estado='pendiente',
        is_active=True
    ).distinct()
    
    #Codigo para traer todas las ganancias realizadas

    años = (
        Pago.objects
        .values_list('fecha_pago__year', flat=True)
        .distinct()
        .order_by('-fecha_pago__year')
    )

    año_seleccionado = request.GET.get('año')

    tabla = []

    if año_seleccionado:
        nombres_meses = [
            'Enero', 'Febrero', 'Marzo', 'Abril',
            'Mayo', 'Junio', 'Julio', 'Agosto',
            'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]

        for mes in range(1, 13):
            pagos_efectivo = Pago.objects.filter(
                activo=True,
                metodo='efectivo',
                estado = 'aprobado',
                fecha_pago__year=año_seleccionado,
                fecha_pago__month=mes
            )

            efectivo = sum(
                pago.cuota.plan.precio
                for pago in pagos_efectivo
            )

            pagos_transferencia = Pago.objects.filter(
                activo=True,
                metodo='transferencia',
                estado = 'aprobado',
                fecha_pago__year=año_seleccionado,
                fecha_pago__month=mes
            )

            transferencia = sum(
                pago.cuota.plan.precio
                for pago in pagos_transferencia
            )

            tabla.append({
                'mes': nombres_meses[mes - 1],
                'efectivo': efectivo,
                'transferencia': transferencia,
                'total': efectivo + transferencia
            })


    return render(request, 'analisis/index.html', {
        'usuarios_activos': usuarios_activos,
        'usuarios_deudores': usuarios_deudores,
        'años': años,
        'año_seleccionado': año_seleccionado,
        'tabla': tabla
    })

