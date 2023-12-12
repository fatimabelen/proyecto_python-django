from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app_coordinadores.models import Coordinador
from .serializers import CoordinadoresSerializer


# Create your views here.

class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadoresSerializer
    permission_clases = [IsAuthenticatedOrReadOnly]