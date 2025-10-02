from django.shortcuts import render
from .models import Juego, Plataforma, Desarrolladora

# Create your views here.
def juegos_list(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/juegos_list.html', {'juegos': juegos})

# Lista de plataformas
def plataformas_list(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'juegos/plataformas_list.html', {'plataformas': plataformas})

# Lista de desarrolladoras
def desarrolladoras_list(request):
    desarrolladoras = Desarrolladora.objects.all()
    return render(request, 'juegos/desarrolladoras_list.html', {'desarrolladoras': desarrolladoras})