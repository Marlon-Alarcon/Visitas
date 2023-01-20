from django.db import models
from apps.maestras.models import Maestra

# Create your models here.

class Persona(models.Model):
    pers_nombre = models.CharField(max_length=30, verbose_name='Nombre')
    pers_apellido = models.CharField(max_length=20, verbose_name='Apellido')
    pers_identificacion = models.CharField(max_length=15, verbose_name='Identificacion')
    tipo_identificacion = models.ForeignKey(Maestra, related_name='tipo_identificacion', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str (self.pers_nombre)

class Estudiante(models.Model):
    estu_edad = models.CharField(max_length=10)
    persona = models.ForeignKey(Persona,null=True, blank=True, on_delete=models.CASCADE )
    tipo_estado = models.ForeignKey(Maestra, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.persona.pers_nombre)


class Visitante(models.Model):
    visit_telefono = models.CharField(max_length=10)
    visit_procedencia = models.CharField(max_length=20)
    persona = models.ForeignKey(Persona, related_name='persona',null=True, blank=True, on_delete=models.CASCADE)
    tipo_parentesco = models.ForeignKey(Maestra, related_name='parentesco', null=True, blank=True, on_delete=models.CASCADE)
    tipo_sexo = models.ForeignKey(Maestra, related_name='sexo',null=True, blank=True, on_delete=models.CASCADE)
    tipo_visitante = models.ForeignKey(Maestra, related_name='visitante',null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str (self.persona)


class Actualizando (models.Model):
    pers = models.ForeignKey(Persona, related_name='pers', null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    accion = models.CharField(max_length=10)

    def __str__(self):
        return str (self.fecha)