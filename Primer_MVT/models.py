from django import utils
from email.policy import default
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50,default = "")
    contraseña = models.CharField(max_length=100,default = "")
    email = models.EmailField()
    fecha_nacimiento = models.DateTimeField()
    
class Posteo(models.Model):
    mensaje = models.TextField(max_length=300, default = "")
    titulo = models.CharField(max_length=40, default = "")
    fecha = models.DateTimeField(default = utils.timezone.now() )#,auto_now_add=True    django.utils.timezone.now
    imagen = models.ImageField(upload_to="imagenes/posteos", null=True, blank=True)

def __str__(self):
    return f"{self.nombre},  {self.emailid}" 
