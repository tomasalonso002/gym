from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .models import UsuarioPersonalizado
from .forms import UsuarioPersonalizadoForm, EditarUsuarioPersonalizadoForm, UsuarioEmpleadoPersonalizadoForm, EditarUsuarioEmpleadoPersonalizadoForm
from cuotas.models import Cuota

from datetime import timedelta
from django.utils import timezone

from django.db.models import Q

# Create your views here.

@login_required
@permission_required('usuarios.add_usuariopersonalizado')
def nuevo_usuario(request):
    if request.method == "POST":
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            dni=form.cleaned_data["dni"]
            if UsuarioPersonalizado.objects.filter(dni=dni, is_active =True).exists():
                form.add_error("dni", "Ya existe un usuario con este dni")
            else:
                usuario = form.save(commit=False)
                usuario.save()
                grupo = Group.objects.get(id=2)
                usuario.groups.add(grupo)

                Cuota.objects.create(
                usuario=usuario,
                plan=usuario.plan,
                fecha_inicio=timezone.now().date(),
                fecha_vencimiento=timezone.now().date() + timedelta(days=30),
                monto=usuario.plan.precio,
                estado='pendiente'
            )
                return redirect('get_usuarios')
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, 'usuarios/nuevo_usuario.html', {'form': form})



@login_required
@permission_required('usuarios.view_usuariopersonalizado')
def get_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.filter(is_active=True, groups__id = 2 )
    query = request.GET.get('q')
    if query:
        usuarios = usuarios.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(dni__icontains=query)
        )
    for usuario in usuarios:
        usuario.cuota_actual = usuario.cuotas.order_by('-fecha_vencimiento').first()
    return render(    
        request,
        'usuarios/get_usuarios.html',
        {'usuarios':usuarios}
    )

@login_required
@permission_required('usuarios.view_usuariopersonalizado')
def get_empleados(request):
    usuarios = UsuarioPersonalizado.objects.filter(is_active=True, groups__id = 3 )
    return render(
        request,
        'usuarios/get_empleados.html',
        {'usuarios':usuarios}
    )

@login_required
@permission_required('usuarios.add_usuariopersonalizado')
def nuevo_empleado(request):
    if request.method == "POST":
        form = UsuarioEmpleadoPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            dni = form.cleaned_data["dni"]
            if UsuarioPersonalizado.objects.filter(dni=dni,is_active =True).exists():
                form.add_error("dni", "Ya existe un empleado con este dni")
            else:
                usuario = form.save(commit=False)
                usuario.save()
                grupo = Group.objects.get(id=3)
                usuario.groups.add(grupo)
                return redirect('get_empleados')
    else:
        form = UsuarioEmpleadoPersonalizadoForm()
    return render(request, 'usuarios/nuevo_empleado.html', {'form': form})




@login_required
@permission_required('usuarios.delete_usuariopersonalizado')
def borrar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPersonalizado, id=id)
    rol = ""
    if usuario.groups.filter(id=2).exists():
        rol = "Usuario"
    else:
        rol = "Empleado"
    if request.method == "POST":
        usuario.is_active = False
        usuario.username = f"{usuario.username}_eliminado_{usuario.id}"
        usuario.save()
        return redirect('get_usuarios')
    return render(request, 'usuarios/borrar_usuario.html', {'usuario':usuario, 'rol':rol})





@login_required
@permission_required('usuarios.change_usuariopersonalizado')
def editar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPersonalizado, id=id)
    if request.method == 'POST':
        form = EditarUsuarioPersonalizadoForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("get_usuarios")
    else:
        form = EditarUsuarioPersonalizadoForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {"form": form})

