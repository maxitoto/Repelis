from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Sum
from django.http import JsonResponse
from django_countries.fields import CountryField
from .choices import TIPODEARTISTA,ESTADODECRITICA

#crear base de datos: python manage.py makemigrate "nombre de la app" despues migrate "nombre de la app" ¡listo!

class Categoria(models.Model):
    categoria=models.CharField(unique=True, max_length=25,null=False,blank=False)

    def __str__(self) -> str:
        return (self.categoria)
    
    
class Artista(models.Model):
    fecha_de_creacion = models.DateTimeField(auto_now_add=True,null=False,blank=False)
    fotografia = models.ImageField(upload_to='artista/', null=True, blank=True)
    nombre = models.CharField(max_length=75,null=False,blank=False)
    apellido = models.CharField(max_length=75,null=False,blank=False)
    fecha_nacimiento = models.DateField(null=False,blank=False) 
    nacionalidad = CountryField(blank_label='(selecciona un país)', null=False, blank=False)
    bibliografia = models.TextField(max_length=700,null=False,blank=True)
    tipo_de_Artista = models.CharField(max_length=10, choices=TIPODEARTISTA, null=False, blank=False, default="ACTOR")
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Pelicula(models.Model):
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)#fecha y hora
    nombre = models.CharField(max_length=100,null=False,blank=False)
    categoria = models.ManyToManyField(Categoria,help_text="Seleccione la/s categoria/s")
    sinopsis = models.TextField(max_length=700, null=False, blank=False)
    cartelera = models.ImageField(upload_to='pelicula/', null=True, blank=True)
    estreno = models.DateField(null=False,blank=False)#fecha   
    rank = models.DecimalField(max_digits=2,decimal_places=1,default=0.0,validators=[MinValueValidator(0.0),MaxValueValidator(5.0)],
    null=False,blank=False)
    pais = CountryField(blank_label='(selecciona un país)', null=False, blank=False)
    artista = models.ManyToManyField(Artista)
    
    def __str__(self) -> str:
        return self.nombre
    
    
class Critica(models.Model):
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100,null=False,blank=False)
    correo = models.EmailField(null=False,blank=False)
    comentario = models.TextField(max_length=1000,null=False,blank=True, default="")
    puntaje = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)],null=False,blank=False)
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE,null=False,blank=False, related_name='criticas')
    estado_de_critica = models.CharField(max_length=11, choices=ESTADODECRITICA, null=False, blank=False, default="EN_REVISION")

    def __str__(self) -> str:
        p = self.pelicula.nombre
        return f"{self.nombre} {self.correo}"

   #redefinicion de save() para actualizar el rank de la pelicula que referencia la critica
    def save(self,*args,**kwargs):
        super(Critica,self).save(*args,**kwargs)#llamo al save original para guardar esta critica
        #momento de actualizar el rank de la pelicula
        nuevoRank = Critica.objects.filter(pelicula=self.pelicula).aggregate(Sum('puntaje'))['puntaje__sum'] / Critica.objects.filter(pelicula=self.pelicula).count()
        self.pelicula.rank=nuevoRank
        self.pelicula.save(update_fields=['rank'])
    
