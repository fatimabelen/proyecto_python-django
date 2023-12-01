from django.db import models
from app_coordinadores import Coordinador
from app_empleados import Empleado
from app_clientes import Cliente
from app_servicios import Servicio

# Create your models here.
class ReservaServicio(models.Model):
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_reservada = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado)
    responsable = models.ForeignKey(Coordinador)

