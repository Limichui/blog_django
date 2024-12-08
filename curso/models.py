from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
import uuid
import os

def unique_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('imagenes/', filename)

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
    duracion = models.IntegerField(validators=[MinValueValidator(1)], help_text="Duración en minutos")
    imagen = models.ImageField(max_length=200, upload_to=unique_image_path, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=Estados.choices, default=Estados.Activo)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    contenido = models.TextField()
    estado = models.CharField(max_length=10, choices=Estados.choices, default=Estados.Activo)
    publicacion = models.ForeignKey("Publicacion", on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comentario por {self.autor} en {self.publicacion}"
    
class Like(models.Model):
    publicacion = models.ForeignKey("Publicacion", on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('publicacion', 'autor')
    
    def __str__(self):
        return f"Like por {self.autor} en {self.publicacion}"
    
