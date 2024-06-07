from typing import Any
from django.views.generic import ListView
from .models import Pelicula

class ViewInicio(ListView):
    model = Pelicula
    template_name = "inicio.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['peliculas']= Pelicula.objects.all()
        return context
        

