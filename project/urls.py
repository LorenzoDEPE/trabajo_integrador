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
from Primer_MVT.views import * #index, monstrar_usuarios, AltaUsuario, BuscarUsuario,enlistar_Posteo,Crear_Posteo,Detalle_Posteo,Actualizar_Posteo,Borrar_posteo,Buscar_Posteo,Iniciar_Sesion,Cerrar_sesion,Crear_usuario,Actualizar_usuario
#, AltaPosteo, mostrar_post, BuscarPosteo,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="inicio"),
    path('usuarios/', monstrar_usuarios), # nueva vista
    path('usuario/alta', AltaUsuario.as_view()),
    path('usuario/buscar', BuscarUsuario.as_view()),
    path('index/', index, name="index-blog"),
    path('list/', ListPost.as_view(), name="list-post"),
    path('create/', CreatePost.as_view(), name="create-post"),
    path('detail/<int:pk>/', DetailPost.as_view(), name="detail-post"),
    path('update/<int:pk>/', UpdatePost.as_view(), name="update-post"),
    path('delete/<int:pk>', DeletePost.as_view(), name="delete-post"),
    path('search-by-name/', SearchPostByName.as_view(), name="search-by-name-post"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('signup/', BlogSignUp.as_view(), name="blog-signup"),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
