from django.db import models
from apps.personas.models import Visitante,Estudiante

# Create your models here.

class Visita(models.Model):
    visi_h_ingreso = models.TimeField()
    visi_h_salida = models.TimeField()
    visi_fecha = models.DateField()
    visitante = models.ForeignKey(Visitante, null=True, blank=True, on_delete=models.CASCADE )
    estudiante = models.ForeignKey(Estudiante, null=True, blank=True, on_delete=models.CASCADE )

    def __str__(self):
        return str (self.visi_h_ingreso)