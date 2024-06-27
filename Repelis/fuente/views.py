from django.urls import reverse
from django.views.generic import ListView,DetailView
from .models import Pelicula,Categoria,Critica,Artista
from django.views.generic.edit import FormMixin
from .forms import Criticar


def categorias_base_dinamico(request):
    return {'categorias': Categoria.objects.all()}


class ViewArtistas(ListView):
    model = Artista
    template_name = 'mostrarArtistas.html'
    context_object_name = 'artistas'

    def get_queryset(self):
        path = self.request.path
        if 'actores' in path:
            return self.model.objects.filter(tipo_de_Artista='ACTOR')
        elif 'directores' in path:
            return self.model.objects.filter(tipo_de_Artista='DIRECTOR')
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'actores' if 'actores' in self.request.path else 'directores'
        return context

        
class ViewArtista(DetailView):
    model = Artista
    template_name = 'mostarArtistaindividual.html'
    context_object_name = 'artista'
    pk_url_kwarg = 'artista_id'

    def get_success_url(self):
        return reverse('ver_artista', kwargs={'artista_id': self.object.pk})


class ViewPeliculas(ListView):
    model = Pelicula
    template_name = 'mostrarPeliculas.html'
    context_object_name = 'peliculas'

    def get_queryset(self):
        categoria = self.kwargs.get('categoria')
        tipo = self.request.path.split('/')[-2]  # Así se obtine la segunda última parte de la URL, preguntar si usar el query es buena practica
        if tipo == 'peliculas':
            return self.model.objects.all()
        elif tipo == categoria:
            peliculas = self.model.objects.all()
            result = []
            for pelicula in peliculas:
                if pelicula.categoria.filter(categoria=categoria).exists():
                    result.append(pelicula)
            return result
        else:  # Si no hay nada o es inicio
            return self.model.objects.order_by('-rank')



class ViewPelicula(DetailView, FormMixin):
    model = Pelicula
    template_name = 'mostrarPeliculaindividual.html'
    context_object_name = 'pelicula'
    pk_url_kwarg = 'pelicula_id'
    form_class = Criticar 


    def get_success_url(self):
        return reverse('ver_pelicula', kwargs={'pelicula_id': self.object.pk})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Agregar el formulario al contexto
        context['criticas'] = self.object.criticas.all()  # Obtener todas las críticas de la película
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # Procesar el formulario válido (guardar crítica, enviar correo, etc.)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pelicula = self.object
        critica = form.save(commit=False)
        critica.pelicula = pelicula
        critica.save()

        # Limpiar el formulario después de que se envíe correctamente
        form.cleaned_data = {}
        return super().form_valid(form)



