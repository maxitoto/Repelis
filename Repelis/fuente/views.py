from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView,FormView,CreateView
from .models import Pelicula,Categoria,Critica,Artista
from django.views.generic.edit import FormMixin
from .forms import Criticar, Registro, IniciarSesion




class ViewArtistas(ListView):
    model = Artista
    template_name = 'mostrarArtistas.html'
    context_object_name = 'artistas'
    paginate_by = 6

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
    paginate_by = 6

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
    paginate_by = 5


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


    
class ViewRegistro(CreateView):
    form_class = Registro
    template_name = 'registro.html'
    success_url = reverse_lazy('solicitudenviada')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        user.save()
        return response   
    
    def form_invalid(self, form):
        # Obtén los errores del formulario
        errors = form.errors.as_data()
        
        # Puedes procesar los errores aquí como desees
        # Por ejemplo, puedes imprimirlos en la consola o guardarlos en un registro
        for field, error_list in errors.items():
            for error in error_list:
                print(f"Error en el campo '{field}': {error}")
        
        # Devuelve la respuesta original del formulario
        return super().form_invalid(form)


from django.contrib.auth.decorators import user_passes_test


def user_in_moderators_group(user):
    return user.is_authenticated and user.groups.filter(name='Moderadores').exists()


class InicioSesionView(FormView):
    form_class = IniciarSesion
    template_name = 'iniciarSesion.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None and user.is_active:
            if user_in_moderators_group(user):
                login(self.request, user)
                return super().form_valid(form)
            else:
                return redirect('espera')  
        else:
            form.add_error(None, "Nombre de usuario o contraseña incorrectos")
            return self.form_invalid(form)
    

def CerrarSesionView(request):
    logout(request)
    return redirect('inicio')
