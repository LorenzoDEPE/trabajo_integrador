from django import forms
from Primer_MVT.models import Usuario
from Primer_MVT.models import Posteo

class UsuarioForm(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_nacimiento']


class PosteoForm(forms.ModelForm):
  class Meta:
    model = Posteo
    fields = ['mensaje', 'titulo', 'fecha']


    
class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)
class BuscarTitulo(forms.Form):
      titulo = forms.CharField(max_length=100)