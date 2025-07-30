from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer



    # prediccion_vivienda/views.py

from django.shortcuts import render

def ver_resultado(request):
    return render(request, 'resultado.html', { 'mensaje': 'Modelo ejecutado correctamente' })
