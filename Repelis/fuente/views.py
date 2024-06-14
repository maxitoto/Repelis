from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Pelicula,Categoria
from .forms import Criticar

def categorias_base_dinamico(request):
    return {'categorias': Categoria.objects.all()}

""" class ViewPeliculas(ListView):
    model = Pelicula
    template_name = "MostrarPeliculas.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['peliculas']= Pelicula.objects.all()
        return context """
    
class ViewPeliculas(ListView):
    model = Pelicula
    template_name = 'mostrarPeliculas.html'
    context_object_name = 'peliculas'

    def get_queryset(self):
        categoria = self.kwargs.get('categoria')
        tipo = self.request.path.split('/')[-2]  # Obtiene la segunda última parte de la URL
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





class pruebaformulario(FormView):
    form_class = Criticar
    template_name = "pruebaCritica.html"
    success_url = "/RedireccionFormularioCorrecto/"
    
    def form_valid(self, form):
        print(form)
        return super().form_valid(form)

