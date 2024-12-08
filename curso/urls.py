from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet, basename='categoria')
router.register(r'publicaciones', views.PublicacionViewSet, basename='publicacion')


urlpatterns = [
    path('', views.index),
    
    # Formularios
    path('categorias_form/', views.categorias, name='categoria'),
    path('publicaciones_form/', views.publicacionFormView, name='publicacion'),
    path('comentarios_form/', views.comentarioFormView, name='comentario'),
    
    # Apis
    path('api/', include(router.urls)),
]