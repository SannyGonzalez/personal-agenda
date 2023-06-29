from django.db import models
from datetime import date

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    fecha = models.DateField(default=date.today)
    lugar = models.CharField(max_length=100)
    contacto_relacionado = models.ForeignKey("contactos.Contacto", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nombre