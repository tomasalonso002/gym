from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ConsultasForm
from .models import Consultas

# Create your views here.
def inicio(request):
    return render(request, "inicio/index.html")


@login_required
@permission_required('inicio.view_consultas')
def get_consultas(request):
    consultas = Consultas.objects.filter(is_active=True).order_by("-id")
    return render(request,'inicio/get_consultas.html',{"consultas":consultas})

def nueva_consulta(request):
    if request.method == "POST":
        form = ConsultasForm(request.POST)
        if form.is_valid():
            form.save()
            form = ConsultasForm()
            redirect("inicio")
    else:
        form = ConsultasForm()
    return render(request, "inicio/nueva_consulta.html", {"form":form})

@login_required
@permission_required('inicio.delete_consultas')
def borrar_consulta(request,id):
    consulta = get_object_or_404(Consultas, id = id)
    if request.method =="POST":
        consulta.is_active = False
        consulta.save()
        return redirect('get_consultas')
    return render(request,'inicio/get_consultas.html')

@login_required
def perfil(request):
    return render(request, 'inicio/perfil.html')