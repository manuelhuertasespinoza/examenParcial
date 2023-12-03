from django.urls import path
from.import views
app_name='gestionTienda'

urlpatterns = [
    path('productos',views.productos,name='productos'),
    path('tiendas',views.tiendas,name='tiendas')
]