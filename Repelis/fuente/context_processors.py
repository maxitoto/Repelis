from django.urls import reverse

links = [
    {"label": "Inicio", "href": reverse("inicio")},
    {"label": "Películas", "href": reverse("peliculas")},
    {"label": "Categorías", "href":"#", "dropdown": True},
    {"label": "Actores", "href":reverse("actores")},
    {"label": "Directores", "href":reverse("directores")},
]


def navbar(request):
    def add_active(link):
        copy = link.copy()
        if copy["href"] == "/":
            copy["active"] = request.path == "/"
        else:
            copy["active"] = request.path.startswith(copy.get("href", ""))
        return copy

    return {"links": map(add_active, links)}




from .models import Categoria
def categorias_base_dinamico(request):
    return {'categorias': Categoria.objects.all()}