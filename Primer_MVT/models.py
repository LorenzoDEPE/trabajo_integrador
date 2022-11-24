from django import utils
from django.db import models

    
class Posteo(models.Model):
    mensaje = models.TextField(max_length=300, default = "")
    titulo = models.CharField(max_length=40, default = "")
    fecha = models.DateTimeField(default = utils.timezone.now ) #,auto_now_add=True    django.utils.timezone.now
    imagen = models.ImageField(upload_to="imagenes/posteos", null=True, blank=True)

