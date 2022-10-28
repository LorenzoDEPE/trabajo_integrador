
from django.shortcuts import render
from django.views import View
from Primer_MVT.models import Usuario,Categoria,Posteo
from Primer_MVT.forms import  UsuarioForm,Buscar,PosteoForm,CategoriaForm,BuscarTitulo

def index(request):
    return render(request, "scripts/index.html") 

def monstrar_usuarios(request):
    lista_usuarios = Usuario.objects.all()
    return render(request, "scripts/usuarios.html", {"lista_usuarios": lista_usuarios})

def mostrar_cat(request):
    lista_cat = Categoria.objects.all()
    return render(request, "scripts/categorias.html", {"lista_cat": lista_cat})

def mostrar_post(request):
    lista_posteos = Posteo.objects.all()
    return render(request, "scripts/Posteos.html", {"lista_posteos": lista_posteos})


class AltaUsuario(View):

    form_class = UsuarioForm
    template_name = 'scripts/form_usuario.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el usuario {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
    
    
class BuscarUsuario(View):

    form_class = Buscar
    template_name = 'scripts/buscar_usuario.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_usuarios = Usuario.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_usuarios':lista_usuarios})
        return render(request, self.template_name, {"form": form})


class AltaPosteo(View):
    
    form_class = PosteoForm
    template_name = 'scripts/form_Posteo.html'
    initial = {"mensaje":"", "titulo":"", "autor":"", "fecha":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el Post {form.cleaned_data.get('titulo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
    
    
class BuscarPosteo(View):

    form_class = BuscarTitulo
    template_name = 'scripts/buscar_posteo.html'
    initial = {"titulo":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            lista_posteos = Posteo.objects.filter(titulo__icontains=titulo).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_posteos':lista_posteos})
        return render(request, self.template_name, {"form": form})

    
class AltaCategoria(View):

    form_class = CategoriaForm
    template_name = 'scripts/form_categoria.html'
    initial = {"nombre":"", "descripcion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la Categoria {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
    
    
class BuscarCategoria(View):

    form_class = Buscar
    template_name = 'scripts/buscar_categoria.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_cat = Categoria.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_cat':lista_cat})
        return render(request, self.template_name, {"form": form})