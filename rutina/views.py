from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from .models import Rutina, RutinaPersonalizada
from usuarios.models import UsuarioPersonalizado
from .forms import RutinaForm,RutinaPersonalizadaForm

@login_required
def rutinas(request):
    rutinas = Rutina.objects.filter(activa=True).order_by('-id')
    mis_rutinas = RutinaPersonalizada.objects.filter(usuario = request.user).order_by('-id')
    return render(request, 'rutina/index.html', {'rutinas': rutinas, 'mis_rutinas':mis_rutinas})


@login_required
@permission_required('rutina.add_rutina')
def crear_rutina(request):
    if request.method == 'POST':
        form = RutinaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rutinas')   
    else:
        form = RutinaForm()
    return render(request, 'rutina/crear_rutina.html', {'form': form})


@login_required
@permission_required('rutina.change_rutina')
def editar_rutina(request, id):
    rutina = get_object_or_404(Rutina, id=id)

    if request.method == 'POST':
        form = RutinaForm(request.POST, instance=rutina)
        if form.is_valid():
            form.save()
            return redirect('rutinas')
    else:
        form = RutinaForm(instance=rutina)

    return render(request, 'rutina/editar_rutina.html', {'form': form, 'rutina': rutina})

@login_required()
@permission_required('rutina.add_rutina')
def crear_rutina_personalizada(request, id):
    if request.method == 'POST':
        form = RutinaPersonalizadaForm(request.POST, request.FILES)
        if form.is_valid():
            rutina = form.save(commit=False)
            rutina.usuario = UsuarioPersonalizado.objects.get(id=id)
            rutina = form.save()
            return redirect('rutinas')   
    else:
        form = RutinaPersonalizadaForm()

    return render(request, 'rutina/crear_rutina_personalizada.html', {'form': form})

@login_required
@permission_required('rutina.delete_rutina')
def eliminar_rutina(request, id):
    rutina = get_object_or_404(Rutina, id=id)
    if request.method == 'POST':
        rutina.activa = False
        rutina.save()
        return redirect('rutinas')
    return render(request, 'rutina/eliminar_rutina.html', {'rutina': rutina})


@login_required
def detalle_rutina(request, id):
    rutina = get_object_or_404(RutinaPersonalizada, id = id)
    return render(request, 'rutina/detalle_rutina.html', {'rutina':rutina})