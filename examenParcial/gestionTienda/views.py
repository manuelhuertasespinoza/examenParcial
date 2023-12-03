from django.shortcuts import render
from .models import tiendas
from .models import productos
# Create your views here.
def productos (request):
    return render(request,'productos.html')

def tiendas (request):
    return render(request,'tiendas.html')