from django.utils.html import format_html
from django.contrib import admin
from .models import Pelicula,Actor,Director,Critica,Categoria
# Register your models here.

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ("imagen_preview", "nombre", "get_categorias", "rank", "estreno")
    search_fields = ("nombre","categoria__categoria")
    list_filter = ('estreno','rank','categoria__categoria')
    date_hierarchy = "estreno"
    list_per_page = 20
    list_max_show_all = 100

    def get_categorias(self, obj):
        # Este método se encarga de buscar las categorías de una película
        return ', '.join(categoria.categoria for categoria in obj.categoria.all())
    
    get_categorias.short_description = 'Categorias'


    def imagen_preview(self, obj):#se encarga de buscar la foto, en esta caso de la pelicula
        if obj.cartelera:
            return format_html('<img src="{}" style="width: 45px; height: 45px;" />', obj.cartelera.url)
        return "No imagen"

    imagen_preview.short_description = 'Imagen'


admin.site.register(Pelicula, PeliculasAdmin)



class actorAdmin(admin.ModelAdmin):
    list_display = ("imagen_preview","nombre","apellido", "nacionalidad") 
    search_fields = ("nombre","apellido", "nacionalidad")
    list_filter = ('nacionalidad',)
    list_per_page = 20
    list_max_show_all = 100

    def imagen_preview(self, obj):
        if obj.fotografia:
            return format_html('<img src="{}" style="width: 45px; height: 45px;" />', obj.fotografia.url)
        return "No Fotografia"

    imagen_preview.short_description = 'Imagen'

admin.site.register(Actor, actorAdmin)

class directorAdmin(admin.ModelAdmin):
    list_display = ("imagen_preview","nombre","apellido", "nacionalidad") 
    search_fields = ("nombre","apellido", "nacionalidad")
    list_filter = ('nacionalidad',)
    list_per_page = 20
    list_max_show_all = 100

    def imagen_preview(self, obj):
        if obj.fotografia:
            return format_html('<img src="{}" style="width: 45px; height: 45px;" />', obj.fotografia.url)
        return "No Fotografia"
    
    imagen_preview.short_description = 'Imagen'
    
admin.site.register(Director, directorAdmin)

class criticaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "puntaje")
    search_fields = ("nombre","correo")
    list_filter = ('puntaje',)
    list_per_page = 50

admin.site.register(Critica, criticaAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display = ("categoria",)
    search_fields = ("categoria",)
    list_per_page = 50
admin.site.register(Categoria, categoriaAdmin)