
from django.shortcuts import render
from django.views import View
from Primer_MVT.models import Familiar,Categoria,Posteo
from Primer_MVT.forms import  FamiliarForm,Buscar,PosteoForm

def index(request):
    return render(request, "scripts/saludar.html") 

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "scripts/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_cat(request):
    lista_cat = Categoria.objects.all()
    return render(request, "scripts/categorias.html", {"lista_cat": lista_cat})

def mostrar_post(request):
    lista_posteos = Posteo.objects.all()
    return render(request, "scripts/Posteos.html", {"lista_posteos": lista_posteos})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'scripts/form_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
    
    
class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'scripts/buscar_familiar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class AltaPosteo(View):
    
    form_class = PosteoForm
    template_name = 'scripts/form_Posteo.html'
    initial = {"mensaje":"", "titulo":"", "autor":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el Post {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})