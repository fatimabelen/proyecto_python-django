from django.db import models

# Create your models here.
class Coordinador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_documento = models.IntegerField()
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)


def __str__(self):
    return F"{self.nombre} | {self.apellido}"
