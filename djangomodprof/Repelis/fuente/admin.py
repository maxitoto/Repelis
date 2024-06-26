from django.utils.html import format_html
from django.contrib import admin 
from django.contrib.admin import SimpleListFilter
from .models import Pelicula,Artista,Critica,Categoria



class RankFilter(SimpleListFilter):
    title = 'calificación' 
    parameter_name = 'rank'

    def lookups(self, request, model_admin):
        return (
            ('muy_buena', 'Muy buena'),
            ('buena', 'Buena'),
            ('normal', 'Normal'),
            ('mala', 'Mala'),
            ('muy_mala', 'Muy mala'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'muy_buena':
            return queryset.filter(rank__gt=4.0)
        if self.value() == 'buena':
            return queryset.filter(rank__gt=3.0, rank__lte=4.0)
        if self.value() == 'normal':
            return queryset.filter(rank__gt=2.0, rank__lte=3.0)
        if self.value() == 'mala':
            return queryset.filter(rank__gt=1.0, rank__lte=2.0)
        if self.value() == 'muy_mala':
            return queryset.filter(rank__lte=1.0)


class PeliculasAdmin(admin.ModelAdmin):
    list_display = ("fecha_de_creacion","imagen_preview", "nombre", "get_categorias", "rank", "estreno","pais")
    search_fields = ("nombre","categoria__categoria","pais")
    list_filter = ('fecha_de_creacion',RankFilter,'categoria__categoria')
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

class artistaAdmin(admin.ModelAdmin):
    list_display = ("fecha_de_creacion","imagen_preview","nombre","apellido","fecha_nacimiento", "nacionalidad","tipo_de_Artista") 
    search_fields = ("nombre","apellido", "nacionalidad")
    list_filter = ('fecha_de_creacion','tipo_de_Artista')
    date_hierarchy = "fecha_nacimiento"
    list_per_page = 20
    list_max_show_all = 100

    def imagen_preview(self, obj):
        if obj.fotografia:
            return format_html('<img src="{}" style="width: 45px; height: 45px;" />', obj.fotografia.url)
        return "No Fotografia"

    imagen_preview.short_description = 'Imagen'

admin.site.register(Artista,artistaAdmin)

class criticaAdmin(admin.ModelAdmin):
    list_display = ("fecha_de_creacion","estado_de_critica","nombre", "correo", "puntaje")
    search_fields = ("fecha_de_creacion", "nombre","correo")
    list_filter = ('puntaje','fecha_de_creacion', 'estado_de_critica',)
    list_per_page = 50

admin.site.register(Critica, criticaAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display = ("categoria",)
    search_fields = ("categoria",)
    list_per_page = 50
admin.site.register(Categoria, categoriaAdmin)