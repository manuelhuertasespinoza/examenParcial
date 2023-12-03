from django.db import models

# Create your models here.
class tiendas(models.Model):
    direccion= models.CharField(max_length=50,blank=True,null=True)
    provincia= models.CharField(max_length=50,blank=True,null=True)
    region= models.CharField(max_length=50,blank=True,null=True)
    fecha_creacion= models.CharField(max_length=50,blank=True,null=True)
    telefono= models.CharField(max_length=9,blank=True,null=True)

class productos(models.Model):
    descripcion= models.CharField(max_length=200,blank=True,null=True)
    codigo= models.CharField(max_length=15,blank=True,null=True)
    pre_venta= models.CharField(max_length=50,blank=True,null=True)
    cantidad= models.CharField(max_length=50,blank=True,null=True)
    tienda_relacionada= models.ForeignKey(tiendas,blank=True,null= True,on_delete=models.SET_NULL)