from django.shortcuts import render

# Create your views here.
def productos (request):
    return render(request,'productos.html')

def tiendas (request):
    return render(request,'tiendas.html')