from django.db import models
from django.urls import reverse


# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)

# Con esta funcion hacemos que cuando agrgamos un objeto nos devuelva el nombre y no como object1, object2, etc...
    def __str__(self):
        return F"{self.id}, {self.apellido.upper()}, {self.nombre}"


    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        return reverse("empleados:detalle", kwargs={"pk": self.pk})
    
