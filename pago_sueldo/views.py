from django.shortcuts import render, get_object_or_404, redirect
from usuarios.models import UsuarioPersonalizado
from .models import CargaHoraria, SueldoHora
from .forms import CargaHorariaForm, SueldoHoraForm


from django.utils import timezone
from datetime import datetime, timedelta


from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

#Funcion que se utiliza para obtener el mes anterior al actual
def obtener_mes_anterior(fecha_actual):
    primer_dia_mes_actual = fecha_actual.replace(day=1)
    mes_anterior = primer_dia_mes_actual - timedelta(days=1)
    primer_dia_mes_anterior = mes_anterior.replace(day=1)
    ultimo_dia_mes_anterior = mes_anterior.replace(day=mes_anterior.day)  # Es decir, el último día del mes anterior
    return primer_dia_mes_anterior, ultimo_dia_mes_anterior


@login_required
@permission_required('usuarios.change_usuariopersonalizado')
def carga_horaria(request, id):
    #Registro de todas las hs que se cargaron hasta el momento
    historial_horas = CargaHoraria.objects.filter(empleado_id=id,activo=True).order_by('-fecha')
    empleado = get_object_or_404(UsuarioPersonalizado, id=id)
    usuario_activo = request.user

    
    fecha_actual = timezone.now()
    primer_dia, ultimo_dia = obtener_mes_anterior(fecha_actual)
    cargas_mes_anterior = CargaHoraria.objects.filter( empleado=empleado, fecha__year=primer_dia.year, fecha__month=primer_dia.month, activo=True)
    total_horas = sum(carga.cantidad for carga in cargas_mes_anterior)


    print("primer dia:", primer_dia)
    print("ultimo dia:", ultimo_dia)
    print(cargas_mes_anterior.count())

    if request.method == 'POST':
        form = CargaHorariaForm(request.POST)
        if form.is_valid():
            carga = form.save(commit=False)
            carga.empleado = empleado
            carga.usuario_activo = usuario_activo
            carga.save()
            return redirect('get_empleados')
    else:
        form = CargaHorariaForm()
    return render(request, 'pago_sueldo/carga_horaria.html',{'empleado':empleado, 'form':form, 'historial_horas': historial_horas, 'total_horas': total_horas, 'mes_anterior': primer_dia.strftime('%B %Y')} )


@login_required
@permission_required('usuarios.change_usuariopersonalizado')
def sueldo_hora(request, id):
    empleado = get_object_or_404(UsuarioPersonalizado, id=id)
    historial_valor = SueldoHora.objects.filter(empleado_id = id,activo=True).order_by('-fecha')
    valor_hora_actual = SueldoHora.objects.filter(empleado_id = id,activo=True).order_by('-fecha').first()
    usuario_activo = request.user
    if request.method == 'POST':
        form = SueldoHoraForm(request.POST)
        if form.is_valid():
            carga =form.save(commit=False)
            carga.empleado = empleado
            carga.usuario_activo = usuario_activo
            carga.save()
            return redirect('get_empleados')
    else:
        form = SueldoHoraForm()
    return render(request, 'pago_sueldo/sueldo_hora.html', {'empleado':empleado, 'historial_valor':historial_valor, 'form':form, 'valor_hora_actual':valor_hora_actual})
