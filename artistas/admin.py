from django.contrib import admin
from .models import Artista, ObraDestacada, HitoLineaTiempo

class ObraDestacadaInline(admin.TabularInline):
    model = ObraDestacada
    extra = 1

class HitoLineaTiempoInline(admin.TabularInline):
    model = HitoLineaTiempo
    extra = 1

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento')
    search_fields = ('nombre', 'biografia')
    inlines = [HitoLineaTiempoInline, ObraDestacadaInline]
@admin.register(ObraDestacada)
class ObraDestacadaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista')
    search_fields = ('titulo', 'artista__nombre')
    list_filter = ('artista',)

@admin.register(HitoLineaTiempo)
class HitoLineaTiempoAdmin(admin.ModelAdmin):
    list_display = ('anio', 'evento', 'artista')
    list_filter = ('artista', 'anio')
    ordering = ('anio',)
