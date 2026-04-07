from django.shortcuts import render
from artistas.models import Artista

def inicio(request):
    # Fetch all artists to display on home page
    artistas = Artista.objects.all().order_by('nombre')
    return render(request, 'core/inicio.html', {'artistas': artistas})

def proyecto(request):
    return render(request, 'core/proyecto.html')

def historia(request):
    return render(request, 'core/historia.html')
