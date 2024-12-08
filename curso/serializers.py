from rest_framework import serializers
from .models import Categoria, Publicacion

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']
        
class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['id', 'titulo', 'contenido', 'duracion', 'imagen', 'estado', 'categoria', 'profesor']
        