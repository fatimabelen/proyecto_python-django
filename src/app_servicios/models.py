from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return F"{self.nombre}"
    
    class META:
        ordering = ['id']
