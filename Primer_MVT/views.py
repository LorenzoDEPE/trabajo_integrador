
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from Primer_MVT.models import Posteo



def about(request):
    return render(request, "scripts/about.html")

  

def index(request):
    posteos = Posteo.objects.order_by('-fecha').all()
    return render(request, 'scripts/index.html', {"Posteos": posteos})

class ListPost(ListView):
    object_list = Posteo.objects.all()
    paginate_by = 2
    model = Posteo
    template_name = 'scripts/posteo_list.html'

class CreatePost(CreateView):
    model=Posteo
    fields = ['titulo', 'fecha', 'mensaje', 'imagen']
    success_url = reverse_lazy("lista-posteos")
    template_name = 'scripts/posteo_form.html'
    
class DetailPost(DetailView):
    model=Posteo
    template_name = 'scripts/posteo_detail.html'

class UpdatePost(UpdateView):
    model = Posteo
    fields = ['titulo', 'fecha', 'mensaje', 'imagen']
    success_url = reverse_lazy("lista-posteos")
    template_name = 'scripts/posteo_form.html'

class DeletePost(DeleteView):
    template_name = 'scripts/posteo_confirm_delete.html'
    model = Posteo
    success_url = reverse_lazy("lista-posteos")

class SearchPostByName(ListView):
    template_name = 'scripts/posteo_list.html'
    def get_queryset(self):
        titulo = self.request.GET.get('post-titulo')
        return Posteo.objects.filter(titulo__icontains=titulo)


class Iniciar_sesion(LoginView):
    template_name = 'scripts/Iniciar_sesion.html'
    next_page = reverse_lazy("lista-posteos")

class BlogLogout(LogoutView):
    template_name = 'scripts/Cerrar_sesion.html'
    
class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "scripts/Crear_usuario.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("login")
    template_name = "scripts/Modificar_usuario.html"
