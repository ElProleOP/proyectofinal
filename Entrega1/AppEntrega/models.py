from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Libros(models.Model):

    genero = models.CharField(max_length=40)
    titulo = models.CharField(max_length=60)
    numero_de_guia = models.IntegerField()
    sinopsis = models.TextField()
    def __str__(self):
        return f'Genero: {self.genero} - Titulo: {self.titulo} - Numero de guia: {self.numero_de_guia}'

class Socio(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

class Juegomesa(models.Model):

    titulo = models.CharField(max_length=40)
    numero_de_guia = models.IntegerField()
    precio = models.IntegerField()

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)


