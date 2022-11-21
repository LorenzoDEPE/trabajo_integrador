
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from Primer_MVT.models import Usuario,Posteo
from Primer_MVT.forms import  UsuarioForm,Buscar,PosteoForm,BuscarTitulo

def index(request):
    return render(request, "scripts/index.html") 

def monstrar_usuarios(request):
    lista_usuarios = Usuario.objects.all()
    return render(request, "scripts/usuarios.html", {"lista_usuarios": lista_usuarios})



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


def index(request):
    posteos = Posteo.objects.order_by('-fecha').all()
    return render(request, 'blog/index.html', {"Posteos": posteos})

class enlistar_Posteo(ListView):
    paginate_by = 2
    model = Posteo

class Crear_Posteo(CreateView):
    model=Posteo
    fields = ['titulo', 'fecha', 'mensaje', 'imagen']
    success_url = reverse_lazy("list-Posteo")
    
class Detalle_Posteo(DetailView):
    model=Posteo

class Actualizar_Posteo(UpdateView):
    model = Posteo
    fields = ['titulo', 'fecha', 'mensaje', 'imagen']
    success_url = reverse_lazy("list-Posteo")

class Borrar_posteo(DeleteView):
    model = Posteo
    success_url = reverse_lazy("list-post")


class Buscar_Posteo(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Posteo.objects.filter(title__icontains=blog_title)


class Iniciar_Sesion(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")

class Cerrar_sesion(LogoutView):
    template_name = 'blog/blog_logout.html'
    
class Crear_usuario(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class Actualizar_usuario(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")
