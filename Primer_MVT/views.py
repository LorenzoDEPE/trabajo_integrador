
from django.shortcuts import render
from django.shortcuts import render
from Primer_MVT.models import Familiar,Categoria

def index(request):
    return render(request, "scripts/saludar.html") 

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    lista_cat = Categoria.objects.all()
    return render(request, "scripts/familiares.html", {"lista_familiares": lista_familiares}, {"lista_cat": lista_cat})