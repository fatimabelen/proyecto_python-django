from rest_framework import serializers
from app_clientes.models import Cliente
from app_coordinadores.models import Coordinador
from app_empleados.models import Empleado
from app_reservas.models import ReservaServicio
from app_servicios.models import Servicio

class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields= '__all__'
        