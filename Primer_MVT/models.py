
from email.policy import default
from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100,default = "")
    direccion = models.CharField(max_length=200,default = "")
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=20,default = "")
    
    
    
class Posteo(models.Model):
    mensaje = models.CharField(max_length=300, default = "")
    titulo = models.CharField(max_length=40, default = "")
    autor =  models.CharField(max_length=100, default = "")
    fecha = models.CharField(max_length=400, default = "")
    
class Categoria(models.Model):
    nombre =  models.CharField(max_length=50, default = "" )
    descripcion =  models.CharField(max_length= 100, default= "")

def __str__(self):
    return f"{self.nombre}, {self.numero_pasaporte}, {self.fecha_nacimiento}, {self.id}", f"{self.nombre}, {self.descripcion}"
