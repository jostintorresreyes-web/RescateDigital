import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

nombres = [
    "Salvador Bustamante Celi",
    "Segundo Cueva Celi",
    "Manuel de Jesús Lozano",
    "Marcos Ochoa Muñoz",
    "Emiliano Ortega Espinosa",
    "David Pacheco Ochoa",
    "Carlos Bonilla Chávez",
    "Segundo Luis Moreno",
    "Benjamín Carrión"
]

bios = {
    "Salvador Bustamante Celi": "Eminente compositor, organista y cantante, y figura fundamental en la música lojana. Su obra abarca valses, pasodobles, yaravíes y música sacra.",
    "Segundo Cueva Celi": "Conocido como el Príncipe del Pasillo. A pesar de perder la visión, su legado es un pilar esencial del pasillo ecuatoriano y lojano.",
    "Manuel de Jesús Lozano": "Compositor lojano con un importante repertorio pianístico, cuyo legado es un aporte valioso al patrimonio musical ecuatoriano.",
    "Marcos Ochoa Muñoz": "Referente de la música lojana y educador musical, con un catálogo compositivo inmenso incluyendo el emblemático pasacalle 'Flor Zamorana'.",
    "Emiliano Ortega Espinosa": "Renombrado escritor, poeta y contribuyente fundamental a la identidad musical y literaria de Loja, autor de las letras de muchas composiciones inmortales.",
    "David Pacheco Ochoa": "Talentoso compositor y docente lojano. Autor de la música y letras de múltiples pasillos, valses y sanjuanitos.",
    "Carlos Bonilla Chávez": "Destacado guitarrista, compositor y contrabajista ecuatoriano, considerado el padre de la guitarra académica en el país.",
    "Segundo Luis Moreno": "Destacado compositor, musicólogo y director de banda. Considerado uno de los pioneros de la musicología en el Ecuador por sus estudios antropológicos y su vasta obra clásica y popular.",
    "Benjamín Carrión": "Insigne escritor, ensayista, diplomático y el mayor promotor cultural lojano y ecuatoriano. Fundador de la Casa de la Cultura Ecuatoriana que potenció decididamente a los artistas nacionales."
}

for nombre in nombres:
    artista, created = Artista.objects.update_or_create(
        nombre=nombre,
        defaults={'biografia': bios.get(nombre, "Biografía en construcción.")}
    )
    if created:
        print(f"Creado: {nombre}")
    else:
        print(f"Actualizado: {nombre}")

print("Proceso de carga de artistas finalizado.")
