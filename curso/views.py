
from django.http import HttpResponse, JsonResponse
from django.db.models import Count

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .forms import PublicacionForm, ComentarioForm
from .models import Categoria, Publicacion, Comentario
from .serializers import CategoriaSerializer, PublicacionSerializer


def index(request):
    return HttpResponse("Blog Aprendea programar")

def categorias(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()
        
    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {
        "categorias": categorias
    })
    
def publicacionFormView(request):
    form = PublicacionForm()
    publicacion = None
    id_pubicacion = request.GET.get('id')
    if id_pubicacion:
        publicacion = get_object_or_404(Publicacion, id=id_pubicacion)
        form = PublicacionForm(instance=publicacion)
    
    if request.method == 'POST':
        if publicacion:
            form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        else:
            form = PublicacionForm(request.POST, request.FILES)
        
    if form.is_valid():
        form.save()
        
    return render(request, "form_publicaciones.html", {"form": form})
    
def comentarioFormView(request):
    form = ComentarioForm()
    comentario = None
    id_comentario = request.GET.get('id')
    if id_comentario:
        comentario = get_object_or_404(Comentario, id=id_comentario)
        form = ComentarioForm(instance=comentario)
    
    if request.method == 'POST':
        if comentario:
            form = ComentarioForm(request.POST, instance=comentario)
        else:
            form = ComentarioForm(request.POST)
        
    if form.is_valid():
        form.save()
        
    return render(request, "form_comentarios.html", {"form": form})
    
# Para ModelViewSet   
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

# Para GenericAPIView
class PublicacionListView(generics.ListAPIView):
    serializer_class = PublicacionSerializer

    def get_queryset(self):
        return Publicacion.objects.filter(estado='Activo')
    
# Para Custom API
@api_view(["GET"])
def categoria_count(request):
    try:
        categorias = Categoria.objects.all()
        data = []

        for categoria in categorias:
            publicaciones_count = Publicacion.objects.filter(categoria=categoria).count()
            data.append({
                "categoria": categoria.nombre,
                "publicaciones_count": publicaciones_count,
            })

        return JsonResponse(data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)
