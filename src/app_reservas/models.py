from django.db import models
from app_coordinadores.models import Coordinador
from app_empleados.models import Empleado
from app_clientes.models import Cliente
from app_servicios.models import Servicio

# Create your models here.
class ReservaServicio(models.Model):
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_reservada = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    responsable = models.ForeignKey(Coordinador, on_delete=models.CASCADE, null=True)

