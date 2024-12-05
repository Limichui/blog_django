from django.db import models

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)
    
class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    duracion = models.IntegerField()
    imagen = models.CharField(max_length=200)
    categoria_id = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)
    
class Comentario(models.Model):
    contenido = models.TextField()
    publicacion_id = models.ForeignKey("Publicacion", on_delete=models.CASCADE)
    
    
