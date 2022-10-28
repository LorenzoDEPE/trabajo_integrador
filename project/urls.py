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
from django.contrib import admin
from django.urls import path
from Primer_MVT.views import AltaPosteo, index, monstrar_familiares, mostrar_cat, AltaFamiliar, BuscarFamiliar, mostrar_post, AltaCategoria, BuscarPosteo, BuscarCategoria


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('familiares/', monstrar_familiares), # nueva vista
    path('categorias/', mostrar_cat), # nueva vista
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('Posteos/', mostrar_post),
    path('Posteos/alta', AltaPosteo.as_view()),
    path('posteos/buscar', BuscarPosteo.as_view()),
    path('categoria/alta', AltaCategoria.as_view()),
    path('categoria/buscar', BuscarCategoria.as_view()),
]
