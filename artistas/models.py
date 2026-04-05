from django.db import models
from django.utils.translation import get_language

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    periodo_vida = models.CharField(max_length=200, blank=True, help_text="Ej: 1 de marzo de 1876 – 1935")
    periodo_vida_en = models.CharField(max_length=200, blank=True)
    periodo_vida_fr = models.CharField(max_length=200, blank=True)
    
    biografia = models.TextField()
    biografia_en = models.TextField(blank=True)
    biografia_fr = models.TextField(blank=True)
    
    composiciones_resumen = models.TextField(blank=True)
    composiciones_resumen_en = models.TextField(blank=True)
    composiciones_resumen_fr = models.TextField(blank=True)
    
    obras_destacadas_resumen = models.TextField(blank=True)
    obras_destacadas_resumen_en = models.TextField(blank=True)
    obras_destacadas_resumen_fr = models.TextField(blank=True)
    
    legado_resumen = models.TextField(blank=True)
    legado_resumen_en = models.TextField(blank=True)
    legado_resumen_fr = models.TextField(blank=True)
    
    imagen_perfil = models.ImageField(upload_to='artistas/', null=True, blank=True)

    def get_translated(self, field_name):
        lang = get_language()
        if lang == 'en':
            attr = f"{field_name}_en"
            val = getattr(self, attr, None)
            if val: return val
        elif lang == 'fr':
            attr = f"{field_name}_fr"
            val = getattr(self, attr, None)
            if val: return val
        return getattr(self, field_name)

    @property
    def translated_nombre(self):
        return self.nombre # Usually names don't change, but can be added if needed

    @property
    def translated_biografia(self):
        return self.get_translated('biografia')

    @property
    def translated_periodo_vida(self):
        return self.get_translated('periodo_vida')

    @property
    def translated_composiciones_resumen(self):
        return self.get_translated('composiciones_resumen')

    @property
    def translated_obras_destacadas_resumen(self):
        return self.get_translated('obras_destacadas_resumen')

    @property
    def translated_legado_resumen(self):
        return self.get_translated('legado_resumen')

    def __str__(self):
        return self.nombre


class ObraDestacada(models.Model):
    titulo = models.CharField(max_length=200)
    titulo_en = models.CharField(max_length=200, blank=True)
    titulo_fr = models.CharField(max_length=200, blank=True)
    
    descripcion = models.TextField(blank=True)
    descripcion_en = models.TextField(blank=True)
    descripcion_fr = models.TextField(blank=True)
    
    archivo_audio = models.FileField(upload_to='audios/', null=True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='obras')

    def get_translated(self, field_name):
        lang = get_language()
        if lang == 'en':
            attr = f"{field_name}_en"
            val = getattr(self, attr, None)
            if val: return val
        elif lang == 'fr':
            attr = f"{field_name}_fr"
            val = getattr(self, attr, None)
            if val: return val
        return getattr(self, field_name)

    def __str__(self):
        return f'{self.titulo} - {self.artista.nombre}'

class HitoLineaTiempo(models.Model):
    anio = models.IntegerField()
    evento = models.CharField(max_length=300)
    evento_en = models.CharField(max_length=300, blank=True)
    evento_fr = models.CharField(max_length=300, blank=True)
    
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='hitos')

    class Meta:
        ordering = ['anio']

    def get_translated(self, field_name):
        lang = get_language()
        if lang == 'en':
            attr = f"{field_name}_en"
            val = getattr(self, attr, None)
            if val: return val
        elif lang == 'fr':
            attr = f"{field_name}_fr"
            val = getattr(self, attr, None)
            if val: return val
        return getattr(self, field_name)

    @property
    def translated_evento(self):
        return self.get_translated('evento')

    def __str__(self):
        return f'{self.anio}: {self.evento[:50]}'


