from django.db import models
from django.core.validators import MinValueValidator

class Estados(models.TextChoices):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    duracion = models.IntegerField(validators=[MinValueValidator(1)])
    imagen = models.ImageField(max_length=200, upload_to='imagenes/')
    estado = models.CharField(max_length=10, choices=Estados.choices, default=Estados.Activo)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    contenido = models.TextField()
    estado = models.CharField(max_length=10, choices=Estados.choices, default=Estados.Activo)
    publicacion = models.ForeignKey("Publicacion", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    
