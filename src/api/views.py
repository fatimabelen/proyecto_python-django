from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_coordinadores.models import Coordinador
from app_clientes.models import Cliente
from .serializers import CoordinadorSerializer, ClienteSerializerList, ClienteSerializerRetrieve


# Create your views here.

# Vistas para COORDINADOR
class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer
    permission_clases = [IsAuthenticatedOrReadOnly]

        
class CoordinadorRetrieveAPIVIEW(generics.RetrieveAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    

# Vistas para CLIENTE
class ClienteListAPIView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializerList
    permission_classes = [IsAuthenticatedOrReadOnly]

class ClienteRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializerRetrieve
    permission_classes = [IsAuthenticatedOrReadOnly]

def api_documentation(request):
    # Aquí puedes proporcionar la información sobre los endpoints de tu API
    return render(request, 'homepages/homepage_apis.html')