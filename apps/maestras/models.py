from django.db import models

# Create your models here.

class Maestra(models.Model):
    maes_nombre = models.CharField(max_length=30)
    maes_valor = models.CharField(max_length=20)
    maes_dependencia = models.CharField(max_length=10)
    maes_tipo_estado = models.CharField(max_length=10)

    def __str__(self):
        return str(self.maes_nombre)