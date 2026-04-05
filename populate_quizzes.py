import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Quiz, Pregunta, Opcion

def populate():
    # Clean previous quizzes
    Quiz.objects.all().delete()
    
    # 1. Historia Básica (10 items)
    q1 = Quiz.objects.create(
        titulo="Historia Básica de la Música Lojana",
        titulo_en="Basic History of Loja Music",
        titulo_fr="Histoire de base de la musique de Loja",
        descripcion="Contesta 10 preguntas sobre géneros e hitos de Loja.",
        descripcion_en="Answer 10 questions about Loja's genres and milestones.",
        descripcion_fr="Répondez à 10 questions sur les genres et les étapes de Loja."
    )
    
    data_q1 = [
        ("¿Apodos de Loja?", "Loja's nicknames?", "Surnoms de Loja?", 
         [("Capital Musical", "Musical Capital", "Capitale Musicale", True), ("Capital Económica", "Economic Capital", "Capitale Économique", False)]),
        ("¿Género tradicional?", "Traditional genre?", "Genre traditionnel?", 
         [("Pasillo", "Pasillo", "Pasillo", True), ("Cumbia", "Cumbia", "Cumbia", False)]),
        ("¿Instrumento común?", "Common instrument?", "Instrument commun?", 
         [("Guitarra", "Guitar", "Guitare", True), ("Batería", "Drums", "Batterie", False)]),
        ("¿Temas en pasillos?", "Themes in pasillos?", "Thématiques des pasillos?", 
         [("Amor y nostalgia", "Love and nostalgia", "Amour et nostalgie", True), ("Guerra", "War", "Guerre", False)]),
        ("¿Evento cultural?", "Cultural event?", "Événement culturel?", 
         [("Artes Vivas", "Live Arts", "Arts Vivants", True), ("Mundial", "World Cup", "Coupe du Monde", False)]),
        ("¿Orquesta de Loja?", "Loja's Orchestra?", "Orchestre de Loja?", 
         [("OSL", "OSL", "OSL", True), ("Banda Blanca", "White Band", "Bande Blanche", False)]),
        ("¿Contexto?", "Context?", "Contexte?", 
         [("Festividades", "Festivities", "Festivités", True), ("Clandestinidad", "Clandestine", "Clandestinité", False)]),
        ("¿Virgen importante?", "Important Virgin?", "Vierge importante?", 
         [("El Cisne", "El Cisne", "El Cisne", True), ("Guadalupe", "Guadalupe", "Guadalupe", False)]),
        ("¿Formato tradicional?", "Traditional format?", "Format traditionnel?", 
         [("Dúo o Trío", "Duo or Trio", "Duo ou Trio", True), ("Heavy Metal", "Heavy Metal", "Heavy Metal", False)]),
        ("¿Qué dice el refrán?", "What does the saying say?", "Que dit le dicton ?", 
         [("Músico de nacimiento", "Musician by birth", "Musicien de naissance", True), ("Nadie es músico", "No one is a musician", "Personne n'est musicien", False)])
    ]

    for p_es, p_en, p_fr, choices in data_q1:
        pregunta = Pregunta.objects.create(quiz=q1, texto_pregunta=p_es, texto_pregunta_en=p_en, texto_pregunta_fr=p_fr)
        for c_es, c_en, c_fr, correct in choices:
            Opcion.objects.create(pregunta=pregunta, texto=c_es, texto_en=c_en, texto_fr=c_fr, es_correcta=correct)

    # 2. Grandes Compositores (10 items)
    q2 = Quiz.objects.create(
        titulo="Grandes Compositores y Artistas",
        titulo_en="Great Composers and Artists",
        titulo_fr="Grands compositeurs et artistes",
        descripcion="Prueba sobre genios musicales de la ciudad.",
        descripcion_en="Test about musical geniuses of the city.",
        descripcion_fr="Test sur les génies musicaux de la ville."
    )
    
    data_q2 = [
        ("¿Nombre del Conservatorio?", "Conservatory name?", "Nom du conservatoire?", [("Bustamante Celi", "Bustamante Celi", "Bustamante Celi", True)]),
        ("¿Formación de músicos?", "Musicians' training?", "Formation des musiciens?", [("Académica", "Academic", "Académique", True)]),
        ("¿Obra de Cueva Celi?", "Cueva Celi's work?", "L'œuvre de Cueva Celi?", [("Pequeña Ciudadana", "Pequeña Ciudadana", "Pequeña Ciudadana", True)]),
        ("¿Música de Himno a Loja?", "Loja Anthem Music?", "Musique de l'hymne de Loja?", [("Bustamante Celi", "Bustamante Celi", "Bustamante Celi", True)]),
        ("¿Letra de Himno a Loja?", "Loja Anthem Lyrics?", "Paroles de l'hymne de Loja?", [("Máximo A. Rodríguez", "Máximo A. Rodríguez", "Máximo A. Rodríguez", True)]),
        ("¿Edgar Palacios toca?", "Edgar Palacios plays?", "Edgar Palacios joue de?", [("Trompeta", "Trumpet", "Trompette", True)]),
        ("¿Grupo Pueblo Nuevo?", "Pueblo Nuevo Group?", "Groupe Pueblo Nuevo?", [("Folklórico", "Folk", "Folklorique", True)]),
        ("¿Pasillo instrumental?", "Instrumental pasillo?", "Pasillo instrumental ?", [("Corazón que no olvida", "Corazón que no olvida", "Corazón que no olvida", True)]),
        ("¿Música sacra antigua?", "Ancient sacred music?", "Musique sacrée ancienne?", [("Archivos Eclesiásticos", "Ecclesiastical Archives", "Archives ecclésiastiques", True)]),
        ("¿Marcos Ochoa Muños?", "Marcos Ochoa Muños?", "Marcos Ochoa Muños?", [("Maestro de Banda", "Band Master", "Maître de fanfare", True)])
    ]
    
    for p_es, p_en, p_fr, choices in data_q2:
        pregunta = Pregunta.objects.create(quiz=q2, texto_pregunta=p_es, texto_pregunta_en=p_en, texto_pregunta_fr=p_fr)
        for c_es, c_en, c_fr, correct in choices:
            Opcion.objects.create(pregunta=pregunta, texto=c_es, texto_en=c_en, texto_fr=c_fr, es_correcta=True)

    # 3. Instrumental y Cronología (10 items)
    q3 = Quiz.objects.create(
        titulo="Instrumental y Cronología",
        titulo_en="Instrumental and Chronology",
        titulo_fr="Instrumentale et chronologie",
        descripcion="Formatos y épocas de maduración sonora.",
        descripcion_en="Formats and eras of sonic maturation.",
        descripcion_fr="Formats et époques de maturation sonore."
    )

    data_q3 = [
        ("¿Fusión siglos XVI-XVIII?", "16th-18th Century fusion?", "Fusion des XVIe-XVIIIe siècles?", [("Andina y Europea", "Andean and European", "Andine et européenne", True)]),
        ("¿Formatos para pasillo?", "Format for pasillo?", "Format pour le pasillo ?", [("Guitarra y Requinto", "Guitar and Requinto", "Guitare et Requinto", True)]),
        ("¿Instrumento andino?", "Andean instrument?", "Instrument andin ?", [("Rondador", "Rondador", "Rondador", True)]),
        ("¿Métrica del pasillo?", "Pasillo metric?", "Métrique du pasillo?", [("3/4 (Vals)", "3/4 (Waltz)", "3/4 (Valse)", True)]),
        ("¿Folklore 1960-1980?", "Folklore 1960-1980?", "Folklore 1960-1980?", [("Radio y Discos", "Radio and Records", "Radio et Disques", True)]),
        ("¿Cuerda frotada?", "Struck string?", "Corde frottée ?", [("Violín", "Violin", "Violon", True)]),
        ("¿Retretas nocturnas?", "Nightly retreats?", "Retraites nocturnes ?", [("Bandas de pueblo", "Village bands", "Fanfares de village", True)]),
        ("¿Baile pasacalle?", "Pasacalle dance?", "Danse pasacalle ?", [("Brazos sueltos", "Loose arms", "Bras lâchés", True)]),
        ("¿Bolero romántico?", "Romantic bolero?", "Boléro romantique ?", [("Competencia pasillo", "Pasillo competition", "Concours de pasillo", True)]),
        ("¿Siglo XXI?", "21st Century?", "XXIe siècle ?", [("Innovación y Jazz", "Innovation and Jazz", "Innovation et jazz", True)])
    ]
    
    for p_es, p_en, p_fr, choices in data_q3:
        pregunta = Pregunta.objects.create(quiz=q3, texto_pregunta=p_es, texto_pregunta_en=p_en, texto_pregunta_fr=p_fr)
        for c_es, c_en, c_fr, correct in choices:
            Opcion.objects.create(pregunta=pregunta, texto=c_es, texto_en=c_en, texto_fr=c_fr, es_correcta=True)

    print("DB recreated with full multilingual supported 3 Quizzes.")

if __name__ == '__main__':
    populate()
