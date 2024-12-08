from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('categorias/', views.categorias, name='categoria'),
    path('publicaciones/', views.publicacionFormView, name='publicacion'),
    path('comentarios/', views.comentarioFormView, name='comentario'),
]