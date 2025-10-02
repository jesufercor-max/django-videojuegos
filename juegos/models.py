from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Juego (models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
class Plataforma (models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    año = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre

class Desarrolladora (models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    juegos_creados = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

