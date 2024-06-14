from django.urls import path
from fuente.views import ViewPeliculas,pruebaformulario

urlpatterns = [
    path('', ViewPeliculas.as_view(), name='inicio'),
    path('categorias/<str:categoria>/', ViewPeliculas.as_view(), name='categoria'),
    path('peliculas/', ViewPeliculas.as_view(), name='peliculas'),
    path('formulario/', pruebaformulario.as_view(), name='pruebaForm'),
]