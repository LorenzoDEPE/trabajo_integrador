from django import forms
from Primer_MVT.models import Familiar

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_nacimiento']
    
    
class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)