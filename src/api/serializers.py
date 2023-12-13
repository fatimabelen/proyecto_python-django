from rest_framework import serializers
from app_clientes.models import Cliente
from app_coordinadores.models import Coordinador
from app_empleados.models import Empleado
from app_reservas.models import ReservaServicio
from app_servicios.models import Servicio

# COORDINADOR
class CoordinadorSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = ['id', 'nombre']

class CoordinadorSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'       

# CLIENTE
class ClienteSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre']

class ClienteSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# SERVICIOS
class ServicioSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre']

class ServicioSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'               
# EMPLEADO
class EmpleadoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre']

class EmpleadoSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'       
