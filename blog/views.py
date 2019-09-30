from django.shortcuts import render, get_object_or_404
from .models import Publicacion
from django.utils import timezone
from .forms import FormPub
from django.shortcuts import redirect

# Create your views here.
def listar_pub(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})

def detalle_pub(request, pk):
    p = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_pub.html', {'pubs':p})

def nueva_pub(request):
    if request.method == "POST":
        f = FormPub(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.autor = request.user
            p.save()
            return redirect('detalle_pub', pk=p.pk)
    else:
        f = FormPub()
    return render(request, 'blog/nueva_pub.html', {'formulario': f})

def editar_pub(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = FormPub(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        form = FormPub(instance=post)
    return render(request, 'blog/nueva_pub.html', {'formulario': form})

def lista_borradores(request):
    posts = Publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/lista_borradores.html', {'posts': posts})

def publicar_publicacion(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.publicar()
    return redirect('detalle_pub', pk=pk)

def eliminar_publicacion(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.delete()
    return redirect('listar_pub')
