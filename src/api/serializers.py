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

# CLIENTES
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

# EMPLEADOS
class EmpleadoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre']

class EmpleadoSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'       

# RESERVAS
class ReservaSerializerList(serializers.ModelSerializer):
    class Meta:
        model = ReservaServicio
        fields = ['id', 'fecha_reservada', 'servicio']

class ReservaSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = ReservaServicio
        fields = '__all__'     