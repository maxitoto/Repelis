from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
import django.utils.timezone
from django.db.models import Sum


class Categoria(models.Model):
    tipo=models.CharField(max_length=25,null=False,blank=False)

    def __str__(self) -> str:
        return (self.tipo)
    

class Director(models.Model):
    fotografia=models.ImageField(null=True)

    nombre=models.CharField(max_length=75,null=False,blank=False)
    apellido=models.CharField(max_length=75,null=False,blank=False)

    nacionalidad=models.CharField(max_length=50,null=False,blank=False)

    bibliografia=models.TextField(max_length=700,null=False,blank=True)
    

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Nacionalidad: {self.nacionalidad}"
    
   

class Actor(models.Model):

    fotografia=models.ImageField(null=True)

    nombre=models.CharField(max_length=75,null=False,blank=False)
    apellido=models.CharField(max_length=75,null=False,blank=False)

    nacionalidad=models.CharField(max_length=50,null=False,blank=False)

    bibliografia=models.TextField(max_length=700,null=False,blank=True)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Nacionalidad: {self.nacionalidad}"

class Pelicula(models.Model):
    nombre=models.CharField(max_length=100,null=False,blank=False)
    
    categoria=models.ManyToManyField(Categoria,help_text="Seleccione la/s categoria/s")
    
    sinopsis=models.TextField(max_length=700,null=False,blank=False)

    cartelera=models.ImageField(null=True)
    
    lanzamiento=models.DateField(null=False,blank=False)   

    rank=models.DecimalField(max_digits=2,decimal_places=1,default=0.0,validators=[MinValueValidator(0.0),MaxValueValidator(5.0)],
    null=False,blank=False)

    actores=models.ManyToManyField(Actor)
    director=models.ManyToManyField(Director)

    def __str__(self) -> str:
        c = ", ".join([str(categoria) for categoria in self.categoria.all()])
        a = ", ".join([f"{actor.nombre} {actor.apellido}" for actor in self.actores.all()])
        d = ", ".join([f"{director.nombre} {director.apellido}" for director in self.director.all()])
        return f"Nombre: {self.nombre}, Categorias: {c}, Fecha: {self.lanzamiento}, Rank: {self.rank}, Sinopsis: {self.sinopsis}, Actores: {a}, Directores: {d}"

class Critica(models.Model):
    nombre=models.CharField(max_length=100,null=False,blank=False)

    correo=models.EmailField(unique=True,null=False,blank=False)

    comentario=models.TextField(max_length=1000,null=True,blank=True #podria ser censurado por un admin
    )
    puntaje=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(10)],null=False,blank=False)
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE,null=False,blank=False)
   
    def __str__(self) -> str:
        p = self.pelicula.nombre
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Comentario: {self.comentario}, Pelicula: {p}, Puntaje: {self.puntaje} "

   #redefinicion de save() para actualizar el rank de la pelicula que referencia la critica
    def save(self,*args,**kwargs):
        super(Critica,self).save(*args,**kwargs)#llamo al save original para guardar esta critica
        #momento de actualizar el rank de la pelicula
        nuevoRank = Critica.objects.filter(pelicula=self.pelicula).aggregate(Sum('puntaje'))['puntaje__sum'] / Critica.objects.filter(pelicula=self.pelicula).count()
        self.pelicula.rank=nuevoRank
        self.pelicula.save(update_fields=['rank'])
    



    

    
    




