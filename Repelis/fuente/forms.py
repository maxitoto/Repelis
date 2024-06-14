from django import forms

class Criticar(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    correo = forms.EmailField(widget=forms.EmailInput)
    critica = forms.CharField(widget=forms.TextInput)

   