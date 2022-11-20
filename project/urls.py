"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Primer_MVT.views import index, monstrar_usuarios, mostrar_cat, AltaUsuario, BuscarUsuario,  AltaCategoria, BuscarCategoria,enlistar_Posteo,Crear_Posteo,Detalle_Posteo,Actualizar_Posteo,Borrar_posteo,Buscar_Posteo,Iniciar_Sesion,Cerrar_sesion,Crear_usuario,Actualizar_usuario
#, AltaPosteo, mostrar_post, BuscarPosteo,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="inicio"),
    path('usuarios/', monstrar_usuarios), # nueva vista
    path('usuario/alta', AltaUsuario.as_view()),
    path('usuario/buscar', BuscarUsuario.as_view()),
    #path('Posteos/', mostrar_post),
    #path('Posteos/alta', AltaPosteo.as_view()),
    #path('posteos/buscar', BuscarPosteo.as_view()),
    path('categorias/', mostrar_cat), # nueva vista
    path('categoria/alta', AltaCategoria.as_view()),
    path('categoria/buscar', BuscarCategoria.as_view()),
    path('list/', enlistar_Posteo.as_view(), name="lista de post"),
    path('create/', Crear_Posteo.as_view(), name="Crear post"),
    path('detail/<int:pk>/', Detalle_Posteo.as_view(), name="Detalle del post"),
    path('update/<int:pk>/', Actualizar_Posteo.as_view(), name="Modificar post"),
    path('delete/<int:pk>', Borrar_posteo.as_view(), name="Eliminar post"),
    path('search-by-name/', Buscar_Posteo.as_view(), name="Buscar post"),
    path('login/', Iniciar_Sesion.as_view(), name="Login"),
    path('logout/', Cerrar_sesion.as_view(), name="Logout"),
    path('signup/', Crear_usuario.as_view(), name="Signup"),
    path('user-profile/<int:pk>', Actualizar_usuario.as_view(), name="Modificar usuario"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
