from django.urls import path
from .views import ver_resultado

urlpatterns = [
    path('modelo/', ver_resultado),
]