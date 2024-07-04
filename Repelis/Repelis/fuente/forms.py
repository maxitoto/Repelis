from django.utils import timezone
from django.forms import EmailInput, PasswordInput, TextInput
from .models import Critica
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms

class Criticar(forms.ModelForm):
    class Meta:
        model = Critica
        fields = ['nombre', 'correo', 'comentario','puntaje']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'puntaje': forms.NumberInput(attrs={
                'class': 'form-range',  
                'min': 1, 
                'max': 5, 
                'step': 1,
                'type': 'range'
            }),
        }


class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.date_joined = timezone.now()
        user.last_login = timezone.now()
        
        if commit:
            user.save()
        return user
            

class IniciarSesion(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


