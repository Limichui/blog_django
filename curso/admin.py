from django.contrib import admin
from .models import Categoria, Publicacion, Comentario

admin.site.register(Categoria)

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'profesor')

admin.site.register(Publicacion)

admin.site.register(Comentario)
