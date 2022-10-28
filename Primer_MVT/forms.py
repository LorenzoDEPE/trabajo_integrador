from django import forms
from Primer_MVT.models import Usuario
from Primer_MVT.models import Posteo
from Primer_MVT.models import Categoria

class UsuarioForm(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_nacimiento']

class PosteoForm(forms.ModelForm):
  class Meta:
    model = Posteo
    fields = ['mensaje', 'titulo', 'autor', 'fecha']

class CategoriaForm(forms.ModelForm):
  class Meta:
    model = Categoria
    fields = ['nombre', 'descripcion']
    
class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)
class BuscarTitulo(forms.Form):
      titulo = forms.CharField(max_length=100)