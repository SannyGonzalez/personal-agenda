from django.db import models
from datetime import date

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=False)
    apellido = models.CharField(max_length=50, blank=True, null=False)
    numero = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=True, null=False)
    grupo = models.CharField(max_length=50, blank=True)
    fecha_inclusion = models.DateField(default=date.today)
    notas = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre