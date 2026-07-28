# Create your views here.
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Cuota,Pago,Plan
from .forms import PagoForm, PlanForm
from datetime import timedelta


@login_required
def cuotas(request):
    cuotas = Cuota.objects.filter(usuario=request.user).order_by('-fecha_vencimiento')
    for cuota in cuotas:
        cuota.ultimo_pago = cuota.pagos.order_by('-fecha_pago').first()
    return render(request, 'cuotas/cuotas.html',{'cuotas': cuotas})

def crear_siguiente_cuota(cuota):
    plan_actual = cuota.usuario.plan
    return Cuota.objects.create(
        usuario=cuota.usuario,
        plan=plan_actual,
        fecha_inicio=cuota.fecha_vencimiento,
        fecha_vencimiento=cuota.fecha_vencimiento + timedelta(days=30),
        monto=plan_actual.precio,
        estado='pendiente'
    )

@permission_required('usuarios.change_usuariopersonalizado')

@login_required
def pagar_cuota(request, id):
    cuota = get_object_or_404(Cuota, id=id, usuario=cuota.usuario)
    if cuota.estado == 'pagada':
        return redirect('get_usuarios')
    cuota.estado = 'pagada'
    cuota.save()
    # evitar duplicar cuota
    existe = Cuota.objects.filter(
        usuario=cuota.usuario,
        fecha_inicio=cuota.fecha_vencimiento
    ).exists()
    if not existe:
        crear_siguiente_cuota(cuota)
    return redirect('get_usuarios')


#Button para que el admin cobre la cuota
@login_required
def pagar_cuota_admin(request, cuota_id):
    cuota = get_object_or_404(Cuota, id=cuota_id)

    if cuota.estado == 'pagada':
        return redirect('detalle_pago_cuota', cuota.usuario.id)

    # crear registro del pago realizado por el admin
    Pago.objects.create(
        cuota=cuota,
        metodo='efectivo',      # o el método que corresponda
        estado='aprobado'
    )

    # marcar la cuota como pagada
    cuota.estado = 'pagada'
    cuota.save()
    print(cuota.plan.nombre)

    # crear la siguiente cuota si no existe
    existe = Cuota.objects.filter(
        usuario=cuota.usuario,
        fecha_inicio=cuota.fecha_vencimiento
    ).exists()

    plan_actual = cuota.usuario.plan
    
    if not existe:
        Cuota.objects.create(
            usuario=cuota.usuario,
            plan=plan_actual,
            fecha_inicio=cuota.fecha_vencimiento,
            fecha_vencimiento=cuota.fecha_vencimiento + timedelta(days=30),
            monto=plan_actual.precio,
            estado='pendiente'
        )
    return redirect('detalle_pago_cuota', cuota.usuario.id)


#Detalle pagar cuota (admin)
@login_required
def detalle_pago_cuota(request, id):
    cuotas = Cuota.objects.filter( usuario_id=id).order_by('-fecha_vencimiento')
    return render(
        request,
        'cuotas/detalle_pago_cuota.html',
        {'cuotas': cuotas}
    )


@login_required
def subir_comprobante(request, cuota_id):
    cuota = get_object_or_404(Cuota,id=cuota_id,usuario=request.user)
    if request.method == 'POST':
        form = PagoForm(request.POST, request.FILES)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.cuota = cuota
            pago.estado = 'pendiente_revision'
            pago.save()
            return redirect('cuotas')
    else:
        form = PagoForm()
    return render(request, 'cuotas/pagar.html', {'form': form, 'cuota': cuota})


def aprobar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    pago.estado = 'aprobado'
    pago.save()

    cuota = pago.cuota
    cuota.estado = 'pagada'
    cuota.save()

    plan_actual = cuota.usuario.plan

    # crear siguiente cuota
    Cuota.objects.create(
        usuario=cuota.usuario,
        plan=plan_actual,
        fecha_inicio=cuota.fecha_vencimiento,
        fecha_vencimiento=cuota.fecha_vencimiento + timedelta(days=30),
        monto=plan_actual.precio,
        estado='pendiente'
    )
    return redirect('pagos_pendientes')

@login_required
def pagos_pendientes(request):
    pagos = Pago.objects.filter(estado='pendiente_revision')
    return render(request, 'cuotas/pagos_pendientes.html', {
        'pagos': pagos
    })


def rechazar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    pago.estado = 'rechazado'
    pago.save()
    return redirect('pagos_pendientes')


#Crear Plan
@login_required
def nuevo_plan(request):
    planes = Plan.objects.filter(activo = True)
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_plan')
    else:
        form = PlanForm()
    return render(request, 'cuotas/nuevo_plan.html',{'planes':planes, 'form':form})

def editar_plan(request,id):
    plan = get_object_or_404(Plan, id=id)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('nuevo_plan')
    else:
        form = PlanForm(instance=plan)
        return render(request, 'cuotas/editar_plan.html', {'form':form})

