import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Quiz, Pregunta, Opcion

quizzes_data = [
    {
        "titulo": "Reto: Salvador Bustamante Celi",
        "titulo_en": "Challenge: Salvador Bustamante Celi",
        "titulo_fr": "Défi : Salvador Bustamante Celi",
        "descripcion": "Preguntas sobre el pionero de Loja.",
        "descripcion_en": "Questions about the pioneer of Loja.",
        "descripcion_fr": "Questions sur le pionnier de Loja.",
        "preguntas": [
            ("¿Nacimiento?", "Birth?", "Naissance ?", [("1876", "1876", "1876", True)]),
            ("¿Instrumento?", "Instrument?", "Instrument ?", [("Órgano", "Organ", "Orgue", True)])
        ]
    },
    {
        "titulo": "Reto: Segundo Cueva Celi",
        "titulo_en": "Challenge: Segundo Cueva Celi",
        "titulo_fr": "Défi : Segundo Cueva Celi",
        "descripcion": "El maestro del pasillo.",
        "descripcion_en": "The master of the pasillo.",
        "descripcion_fr": "Le maître du pasillo.",
        "preguntas": [
            ("¿Pasillo famoso?", "Famous pasillo?", "Pasillo célèbre ?", [("Vaso de Lágrimas", "Vaso de Lágrimas", "Vaso de Lágrimas", True)])
        ]
    },
    {
        "titulo": "Reto: Manuel de Jesús Lozano",
        "titulo_en": "Challenge: Manuel de Jesús Lozano",
        "titulo_fr": "Défi : Manuel de Jesús Lozano",
        "descripcion": "Pilar tradicional.",
        "descripcion_en": "Traditional pillar.",
        "descripcion_fr": "Pilier traditionnel.",
        "preguntas": [
            ("¿Época?", "Era?", "Époque ?", [("S. XX", "20th C.", "XXe s.", True)])
        ]
    }
]

# Adding placeholder quizzes for the rest to ensure they exist and are translated
rest_artists = [
    "Marcos Ochoa Muñoz", "Emiliano Ortega", "Víctor Moreno Proaño", 
    "Daniel Armijos Carrión", "David Pacheco Ochoa", "Julio Cañar", "Francisco Rodas Bustamante"
]

for name in rest_artists:
    quizzes_data.append({
        "titulo": f"Reto: {name}",
        "titulo_en": f"Challenge: {name}",
        "titulo_fr": f"Défi : {name}",
        "descripcion": f"¿Cuánto sabes de {name}?",
        "descripcion_en": f"How much do you know about {name}?",
        "descripcion_fr": f"Que savez-vous de {name} ?",
        "preguntas": [
            (f"¿Quién fue {name}?", f"Who was {name}?", f"Qui était {name} ?", [(f"Un gran músico", "A great musician", "Un grand musicien", True)])
        ]
    })

for q_data in quizzes_data:
    quiz, created = Quiz.objects.get_or_create(
        titulo=q_data["titulo"],
        defaults={
            "titulo_en": q_data["titulo_en"],
            "titulo_fr": q_data["titulo_fr"],
            "descripcion": q_data["descripcion"],
            "descripcion_en": q_data.get("descripcion_en", ""),
            "descripcion_fr": q_data.get("descripcion_fr", "")
        }
    )
    if not created:
        quiz.preguntas.all().delete()
    
    for p_es, p_en, p_fr, choices in q_data["preguntas"]:
        pregunta = Pregunta.objects.create(quiz=quiz, texto_pregunta=p_es, texto_pregunta_en=p_en, texto_pregunta_fr=p_fr)
        for c_es, c_en, c_fr, correct in choices:
            Opcion.objects.create(pregunta=pregunta, texto=c_es, texto_en=c_en, texto_fr=c_fr, es_correcta=correct)

print("All artist-specific quizzes updated with EN and FR.")
