from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=6)
    activo = models.BooleanField(default=True)