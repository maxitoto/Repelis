from django.contrib import admin
from .models import Pelicula,Actor,Director,Critica,Categoria
# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Critica)
admin.site.register(Categoria)