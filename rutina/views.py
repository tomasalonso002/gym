from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from .models import Rutina
from .forms import RutinaForm

@login_required
def rutinas(request):
    print(request.user.get_all_permissions())
    rutinas = Rutina.objects.filter(activa=True).order_by('-id')
    return render(request, 'rutina/index.html', {'rutinas': rutinas})


@login_required
@permission_required('rutina.add_rutina')
def crear_rutina(request):
    if request.method == 'POST':
        form = RutinaForm(request.POST)
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


@login_required
@permission_required('rutina.delete_rutina')
def eliminar_rutina(request, id):
    rutina = get_object_or_404(Rutina, id=id)
    if request.method == 'POST':
        rutina.activa = False
        rutina.save()
        return redirect('rutinas')

    return render(request, 'rutina/eliminar_rutina.html', {'rutina': rutina})