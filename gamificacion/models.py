from django.db import models
from django.utils.translation import get_language

class Quiz(models.Model):
    titulo = models.CharField(max_length=200)
    titulo_en = models.CharField(max_length=200, blank=True)
    titulo_fr = models.CharField(max_length=200, blank=True)
    
    descripcion = models.TextField(blank=True)
    descripcion_en = models.TextField(blank=True)
    descripcion_fr = models.TextField(blank=True)

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
    def translated_titulo(self):
        return self.get_translated('titulo')

    @property
    def translated_descripcion(self):
        return self.get_translated('descripcion')

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='preguntas')
    texto_pregunta = models.CharField(max_length=300)
    texto_pregunta_en = models.CharField(max_length=300, blank=True)
    texto_pregunta_fr = models.CharField(max_length=300, blank=True)

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
    def translated_texto_pregunta(self):
        return self.get_translated('texto_pregunta')

    def __str__(self):
        return self.texto_pregunta

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=200)
    texto_en = models.CharField(max_length=200, blank=True)
    texto_fr = models.CharField(max_length=200, blank=True)
    es_correcta = models.BooleanField(default=False)

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
    def translated_texto(self):
        return self.get_translated('texto')

    def __str__(self):
        return f'{self.texto} ({"Correcta" if self.es_correcta else "Incorrecta"})'


class Logro(models.Model):
    nombre = models.CharField(max_length=150)
    nombre_en = models.CharField(max_length=150, blank=True)
    nombre_fr = models.CharField(max_length=150, blank=True)
    
    descripcion = models.TextField()
    descripcion_en = models.TextField(blank=True)
    descripcion_fr = models.TextField(blank=True)
    
    puntos_requeridos = models.IntegerField()
    icono = models.ImageField(upload_to='logros/', null=True, blank=True)

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
        return self.get_translated('nombre')

    @property
    def translated_descripcion(self):
        return self.get_translated('descripcion')

    def __str__(self):
        return f'{self.nombre} ({self.puntos_requeridos} pts)'

class ResultadoQuiz(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    puntos = models.IntegerField()
    fecha_completado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'quiz')
        verbose_name_plural = "Resultados de Quizzes"

    def __str__(self):
        return f'{self.usuario.username} - {self.quiz.titulo} ({self.puntos} pts)'

