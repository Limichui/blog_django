from django.contrib import admin
from .models import Categoria, Publicacion, Comentario

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_registro')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    
    def fecha_registro(self, obj): 
        return obj.created 
    fecha_registro.short_description = 'Fecha Registro'
    
admin.site.register(Categoria, CategoriaAdmin)

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracion', 'estado', 'categoria', 'profesor')
    ordering = ('titulo',)
    search_fields = ('titulo',)
    list_filter = ('estado',)

admin.site.register(Publicacion, PublicacionAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'autor', 'estado', 'publicacion', 'fecha_registro')
    ordering = ('-created',) # Orden descendente por el campo 'created' es con '-created'
    search_fields = ('contenido',)
    list_filter = ('estado',)
    
    def fecha_registro(self, obj): 
        return obj.created 
    fecha_registro.short_description = 'Fecha Registro'
    
admin.site.register(Comentario, ComentarioAdmin)
