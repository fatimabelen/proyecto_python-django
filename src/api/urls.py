from django.urls import path
from .views import CoordinadorListAPIView

app_name = 'api'

urlpatterns = [
    path('coordinadores/', CoordinadorListAPIView.as_view(), name='listar_coordinadores'),
]
