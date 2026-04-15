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

from django.core.management import call_command
from django.http import HttpResponse

def run_migrations(request):
    try:
        call_command('migrate', interactive=False)
        return HttpResponse("Migrations applied successfully!")
    except Exception as e:
        return HttpResponse(f"Migration failed: {e}")
