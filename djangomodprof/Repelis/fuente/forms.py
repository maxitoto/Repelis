from django import forms
from .models import Critica

class Criticar(forms.ModelForm):
    class Meta:
        model = Critica
        fields = ['nombre', 'correo', 'comentario','puntaje']

   