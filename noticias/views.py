
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Noticias
from .forms import NoticiasForm
# Create your views here.

@login_required
def noticias(request):
    noticias = Noticias.objects.filter(activa=True).order_by('-id')
    return render(request, 'noticias/index.html',{'noticias':noticias})

@login_required
@permission_required('noticias.add_noticias')
def nueva_noticia(request):
    usuario_activo = request.user
    if request.method == 'POST':
        form = NoticiasForm(request.POST, request.FILES)
        if form.is_valid():
             noticia = form.save(commit=False)
             noticia.usuario = usuario_activo
             noticia.save()
             return redirect('noticias')
    else:
        form = NoticiasForm()
    return render(request, 'noticias/nueva_noticia.html',{'form':form})

@login_required
@permission_required('noticias.delete_noticias')
def borrar_noticia(request, id):
    noticia = get_object_or_404(Noticias, id = id)
    if request.method == "POST":
        noticia.activa = False
        noticia.save()
        return redirect('noticias')
    return render(request, 'noticias/borrar_noticia.html', {'noticia':noticia})

