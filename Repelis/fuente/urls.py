from django.urls import path
from fuente.views import ViewPeliculas, ViewPelicula, ViewArtistas, ViewArtista
from django.views.generic import TemplateView

urlpatterns = [
    path('', ViewPeliculas.as_view(), name='inicio'),
    path('categorias/<str:categoria>/', ViewPeliculas.as_view(), name='categoria'),
    path('peliculas/', ViewPeliculas.as_view(), name='peliculas'),
    path('pelicula/<int:pelicula_id>/', ViewPelicula.as_view(), name='ver_pelicula'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),
    path('actores/', ViewArtistas.as_view(), name='actores'),
    path('directores/', ViewArtistas.as_view(), name='directores'),
    path('actores/<int:artista_id>/', ViewArtista.as_view(), name='ver_actor'),
    path('directores/<int:artista_id>/', ViewArtista.as_view(), name='ver_director'),
]