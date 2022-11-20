from django import utils
from email.policy import default
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100,default = "")
    direccion = models.CharField(max_length=200,default = "")
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento = models.CharField(max_length=20,default = "")
    
class Posteo(models.Model):
    mensaje = models.TextField(max_length=300, default = "")
    titulo = models.CharField(max_length=40, default = "")
    fecha = models.DateTimeField(default = utils.timezone.now() )#,auto_now_add=True    django.utils.timezone.now
    imagen = models.ImageField(upload_to="imagenes/posteos", null=True, blank=True)
    
class Categoria(models.Model):
    nombre =  models.CharField(max_length=50, default = "" )
    descripcion =  models.CharField(max_length= 100, default= "")

def __str__(self):
    return f"{self.nombre}, {self.numero_pasaporte}, {self.fecha_nacimiento}, {self.id}" f"{self.nombre}, {self.descripcion}"
