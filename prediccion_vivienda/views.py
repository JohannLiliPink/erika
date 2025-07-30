from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .ml.modelo import entrenar_modelo

from decouple import config
from fredapi import Fred

FRED_API_KEY = config('FRED_API_KEY')
fred = Fred(api_key=FRED_API_KEY)

def ver_resultado(request):
    
    resultado = entrenar_modelo()

    return render( request ,  'resultado.html' , {'resultado': resultado} )