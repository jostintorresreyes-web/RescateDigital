import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Quiz, Pregunta, Opcion

def populate():
    # Clean previous quizzes
    Quiz.objects.all().delete()
    
    # ----------------------------------------------------
    # QUIZ 1: HISTORIA BÁSICA DE LA MÚSICA LOJANA (10 items)
    # ----------------------------------------------------
    q1 = Quiz.objects.create(
        titulo="Historia Básica de la Música Lojana",
        descripcion="Demuestra tus conocimientos generales sobre los orígenes, géneros e hitos que han marcado a Loja."
    )
    
    p1_1 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Cuáles son los apodos o denominaciones que recibe Loja en el Ecuador?")
    Opcion.objects.create(pregunta=p1_1, texto="Capital Económica del Ecuador", es_correcta=False)
    Opcion.objects.create(pregunta=p1_1, texto="Capital Musical y Cultural del Ecuador", es_correcta=True)
    Opcion.objects.create(pregunta=p1_1, texto="La Atenas del Ecuador", es_correcta=False)

    p1_2 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Cuáles son algunos géneros musicales tradicionales del Ecuador?")
    Opcion.objects.create(pregunta=p1_2, texto="La cumbia", es_correcta=False)
    Opcion.objects.create(pregunta=p1_2, texto="El Pasillo", es_correcta=True)
    Opcion.objects.create(pregunta=p1_2, texto="La bomba del Chota", es_correcta=False)

    p1_3 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Cuáles son instrumentos musicales comunes en la interpretación de música tradicional?")
    Opcion.objects.create(pregunta=p1_3, texto="La guitarra acústica", es_correcta=True)
    Opcion.objects.create(pregunta=p1_3, texto="La batería", es_correcta=False)
    Opcion.objects.create(pregunta=p1_3, texto="El saxofón", es_correcta=False)

    p1_4 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Qué temas suelen predominar en la música tradicional ecuatoriana?")
    Opcion.objects.create(pregunta=p1_4, texto="El amor, el desamor y la nostalgia poética", es_correcta=True)
    Opcion.objects.create(pregunta=p1_4, texto="Las victorias militares en guerras mundiales", es_correcta=False)
    Opcion.objects.create(pregunta=p1_4, texto="El humor sarcástico contra los políticos", es_correcta=False)

    p1_5 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Cuáles son eventos importantes relacionados con la cultura y el arte en el Ecuador?")
    Opcion.objects.create(pregunta=p1_5, texto="El Festival Internacional de Artes Vivas", es_correcta=True)
    Opcion.objects.create(pregunta=p1_5, texto="El Mundial de Fútbol", es_correcta=False)
    Opcion.objects.create(pregunta=p1_5, texto="La Fiesta de las Flores y las Frutas", es_correcta=False)

    p1_6 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Qué agrupaciones musicales reconocidas existen en el país?")
    Opcion.objects.create(pregunta=p1_6, texto="La Orquesta Sinfónica de Guayaquil", es_correcta=False)
    Opcion.objects.create(pregunta=p1_6, texto="La Orquesta Sinfónica de Loja (OSL)", es_correcta=True)
    Opcion.objects.create(pregunta=p1_6, texto="La Banda Blanca de la Marina", es_correcta=False)

    p1_7 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿En qué contextos suele interpretarse la música tradicional ecuatoriana?")
    Opcion.objects.create(pregunta=p1_7, texto="En contextos religiosos, festividades locales y retretas", es_correcta=True)
    Opcion.objects.create(pregunta=p1_7, texto="Solo de manera clandestina", es_correcta=False)
    Opcion.objects.create(pregunta=p1_7, texto="Exclusivamente en partidos de índor fútbol", es_correcta=False)

    p1_8 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Qué advocaciones marianas son importantes en la religiosidad ecuatoriana?")
    Opcion.objects.create(pregunta=p1_8, texto="La Virgen de Guadalupe", es_correcta=False)
    Opcion.objects.create(pregunta=p1_8, texto="La Virgen de El Cisne", es_correcta=True)
    Opcion.objects.create(pregunta=p1_8, texto="La Virgen del Panecillo", es_correcta=False)

    p1_9 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Cuáles son formatos comunes de agrupaciones musicales tradicionales?")
    Opcion.objects.create(pregunta=p1_9, texto="El dúo o trío", es_correcta=True)
    Opcion.objects.create(pregunta=p1_9, texto="La banda de heavy metal", es_correcta=False)
    Opcion.objects.create(pregunta=p1_9, texto="El cuarteto de djs", es_correcta=False)

    p1_10 = Pregunta.objects.create(quiz=q1, texto_pregunta="¿Qué frases populares reflejan la identidad musical de Loja?")
    Opcion.objects.create(pregunta=p1_10, texto="'Si un lojano no toca la guitarra, no existe.'", es_correcta=False)
    Opcion.objects.create(pregunta=p1_10, texto="'El que no toca guitarra puede cantar una canción.' (Referencia al talento innato)", es_correcta=True)
    Opcion.objects.create(pregunta=p1_10, texto="'Nadie nace músico en Loja'", es_correcta=False)


    # ----------------------------------------------------
    # QUIZ 2: GRANDES COMPOSITORES LOJANOS (10 items)
    # ----------------------------------------------------
    q2 = Quiz.objects.create(
        titulo="Grandes Compositores y Artistas Lojanos",
        descripcion="¿Qué tanto conoces sobre las mentes brillantes y artistas emblemáticos del legado musical lojano?"
    )

    p2_1 = Pregunta.objects.create(quiz=q2, texto_pregunta="¿De qué gran maestro lleva su nombre la institución académica Conservatorio Nacional de Música en Loja?")
    Opcion.objects.create(pregunta=p2_1, texto="Julio Jaramillo", es_correcta=False)
    Opcion.objects.create(pregunta=p2_1, texto="Segundo Cueva Celi", es_correcta=False)
    Opcion.objects.create(pregunta=p2_1, texto="Salvador Bustamante Celi", es_correcta=True)

    p2_2 = Pregunta.objects.create(quiz=q2, texto_pregunta="¿Qué distinción particular tienen la mayoría de compositores clásicos de la Época de Oro lojana?")
    Opcion.objects.create(pregunta=p2_2, texto="Nunca escribieron sus obras por rechazo a lo occidental", es_correcta=False)
    Opcion.objects.create(pregunta=p2_2, texto="Eran músicos autodidactas", es_correcta=False)
    Opcion.objects.create(pregunta=p2_2, texto="Tenían una profunda formación académica de notación y conservatorio", es_correcta=True)

    p2_3 = Pregunta.objects.create(quiz=q2, texto_pregunta="Segundo Cueva Celi es una de las figuras pilar de Ecuador por:")
    Opcion.objects.create(pregunta=p2_3, texto="Componer pasillos sublimes e inolvidables como 'Pequeña Ciudadana'", es_correcta=True)
    Opcion.objects.create(pregunta=p2_3, texto="Descubrir el pasillo costeño", es_correcta=False)
    Opcion.objects.create(pregunta=p2_3, texto="Fusionar por primera vez el pasillo con el trap", es_correcta=False)

    p2_4 = Pregunta.objects.create(quiz=q2, texto_pregunta="¿Quién es el autor de la música del glorioso 'Himno a Loja'?")
    Opcion.objects.create(pregunta=p2_4, texto="Segundo Cueva Celi", es_correcta=False)
    Opcion.objects.create(pregunta=p2_4, texto="Salvador Bustamante Celi", es_correcta=True)
    Opcion.objects.create(pregunta=p2_4, texto="Carlos Rubira Infante", es_correcta=False)

    p2_5 = Pregunta.objects.create(quiz=q2, texto_pregunta="¿Quién escribió la estrofa y letra poética del Himno a Loja?")
    Opcion.objects.create(pregunta=p2_5, texto="Máximo Agustín Rodríguez", es_correcta=True)
    Opcion.objects.create(pregunta=p2_5, texto="Juan León Mera", es_correcta=False)
    Opcion.objects.create(pregunta=p2_5, texto="Miguel Riofrío", es_correcta=False)

    p2_6 = Pregunta.objects.create(quiz=q2, texto_pregunta="Edgar Palacios, ícono y maestro lojano, es reconocido a escala global como un virtuoso de:")
    Opcion.objects.create(pregunta=p2_6, texto="La trompeta", es_correcta=True)
    Opcion.objects.create(pregunta=p2_6, texto="El fagot", es_correcta=False)
    Opcion.objects.create(pregunta=p2_6, texto="El contrabajo", es_correcta=False)

    p2_7 = Pregunta.objects.create(quiz=q2, texto_pregunta="El emblemático y aplaudido grupo folklórico musical formado por lojanos en Quito se llama:")
    Opcion.objects.create(pregunta=p2_7, texto="Kjarkas", es_correcta=False)
    Opcion.objects.create(pregunta=p2_7, texto="Grupo Pueblo Nuevo", es_correcta=True)
    Opcion.objects.create(pregunta=p2_7, texto="Ñanda Mañachi", es_correcta=False)

    p2_8 = Pregunta.objects.create(quiz=q2, texto_pregunta="¿Cómo se denomina al pasillo nostálgico instrumental cuyas famosas versiones provienen del maestro Cueva Celi?")
    Opcion.objects.create(pregunta=p2_8, texto="'Corazón que no olvida'", es_correcta=True)
    Opcion.objects.create(pregunta=p2_8, texto="'El Aguacate'", es_correcta=False)
    Opcion.objects.create(pregunta=p2_8, texto="'Sombras'", es_correcta=False)

    p2_9 = Pregunta.objects.create(quiz=q2, texto_pregunta="Gran parte de las composiciones de música sacra que datan de la etapa pre-republicana son guardadas por:")
    Opcion.objects.create(pregunta=p2_9, texto="Las disqueras modernas de Ecuador", es_correcta=False)
    Opcion.objects.create(pregunta=p2_9, texto="Las familias fundadoras y los Archivos Eclesiásticos y de los Conventos en Loja", es_correcta=True)
    Opcion.objects.create(pregunta=p2_9, texto="Nunca fueron guardadas y todas se quemaron", es_correcta=False)

    p2_10 = Pregunta.objects.create(quiz=q2, texto_pregunta="Marcos Ochoa Muñoz es recordado en Loja por ser un gran maestro de:")
    Opcion.objects.create(pregunta=p2_10, texto="Pintura abstracta", es_correcta=False)
    Opcion.objects.create(pregunta=p2_10, texto="Piano, percusión, armonía y destacadísimo forjador de músicos de banda", es_correcta=True)
    Opcion.objects.create(pregunta=p2_10, texto="Gastronomía ecuatoriana", es_correcta=False)


    # ----------------------------------------------------
    # QUIZ 3: INSTRUMENTAL Y CRONOLOGÍA (10 items)
    # ----------------------------------------------------
    q3 = Quiz.objects.create(
        titulo="Instrumental y Evolución Cronológica",
        descripcion="Diferencia la evolución de los formatos musicales y las diferentes épocas de maduración sonora de Loja."
    )

    p3_1 = Pregunta.objects.create(quiz=q3, texto_pregunta="¿Qué suceso generó el desarrollo inicial de una identidad propia durante los siglos XVI al XVIII en la región sur?")
    Opcion.objects.create(pregunta=p3_1, texto="La importación de salsa centroamericana", es_correcta=False)
    Opcion.objects.create(pregunta=p3_1, texto="La fusión y mezcla entre los ritmos andinos nativos y las formas e instrumentos europeos", es_correcta=True)
    Opcion.objects.create(pregunta=p3_1, texto="La prohibición de instrumentos de cuerda", es_correcta=False)

    p3_2 = Pregunta.objects.create(quiz=q3, texto_pregunta="El formato principal más reconocido y utilizado para dar contexto a la voz principal de un pasillo es:")
    Opcion.objects.create(pregunta=p3_2, texto="Bajo sinfónico, tambor mayor y sintetizador", es_correcta=False)
    Opcion.objects.create(pregunta=p3_2, texto="Guitarra y Requinto", es_correcta=True)
    Opcion.objects.create(pregunta=p3_2, texto="Flauta dulce europea antigua", es_correcta=False)

    p3_3 = Pregunta.objects.create(quiz=q3, texto_pregunta="¿Qué instrumento de viento andino era el más común en las festividades indígenas locales mucho antes de la república?")
    Opcion.objects.create(pregunta=p3_3, texto="El Rondador o pinguillo", es_correcta=True)
    Opcion.objects.create(pregunta=p3_3, texto="La Tuba", es_correcta=False)
    Opcion.objects.create(pregunta=p3_3, texto="El Clarinete metálico", es_correcta=False)

    p3_4 = Pregunta.objects.create(quiz=q3, texto_pregunta="¿Cuál de las siguientes es una métrica empleada originalmente en el pasillo lojano de salón?")
    Opcion.objects.create(pregunta=p3_4, texto="Medio compás de cumbia", es_correcta=False)
    Opcion.objects.create(pregunta=p3_4, texto="Ritmo fuertemente acelerado estilo mambo", es_correcta=False)
    Opcion.objects.create(pregunta=p3_4, texto="Compás tradicional de 3/4 derivado del vals europeo", es_correcta=True)

    p3_5 = Pregunta.objects.create(quiz=q3, texto_pregunta="Las décadas de 1960-1980 propulsaron el folklore lojano gracias a:")
    Opcion.objects.create(pregunta=p3_5, texto="La radio local y la creciente facilidad de registros sonoros (discos y casetes)", es_correcta=True)
    Opcion.objects.create(pregunta=p3_5, texto="La creación de plataformas como Spotify", es_correcta=False)
    Opcion.objects.create(pregunta=p3_5, texto="La abolición del cine mudo", es_correcta=False)

    p3_6 = Pregunta.objects.create(quiz=q3, texto_pregunta="Instrumento de cuerda frotada de origen europeo y sumamente indispensable en la época orquestal lojana temprana:")
    Opcion.objects.create(pregunta=p3_6, texto="La batería", es_correcta=False)
    Opcion.objects.create(pregunta=p3_6, texto="El violín", es_correcta=True)
    Opcion.objects.create(pregunta=p3_6, texto="La percusión africana", es_correcta=False)

    p3_7 = Pregunta.objects.create(quiz=q3, texto_pregunta="Aparte de las serenatas bohemias bajo balcones, ¿qué otra gran actividad musical nocturna al aire libre congregaba a la gente lojana?")
    Opcion.objects.create(pregunta=p3_7, texto="Las presentaciones en televisión privada", es_correcta=False)
    Opcion.objects.create(pregunta=p3_7, texto="Las 'retretas' de bandas de pueblo y municipales en los parques centrales", es_correcta=True)
    Opcion.objects.create(pregunta=p3_7, texto="Los concursos de rap estilo libre", es_correcta=False)

    p3_8 = Pregunta.objects.create(quiz=q3, texto_pregunta="En el baile tradicional, ¿el pasacalle lojano se danza agarrado permanentemente o usualmente de brazos sueltos?")
    Opcion.objects.create(pregunta=p3_8, texto="Totalmente sueltos, dinámicos, levantando un pañuelo o entrelazando manos rápidamente", es_correcta=True)
    Opcion.objects.create(pregunta=p3_8, texto="Firmemente abrazados sin despegarse como el tango", es_correcta=False)
    Opcion.objects.create(pregunta=p3_8, texto="Bailando sin mover los brazos", es_correcta=False)

    p3_9 = Pregunta.objects.create(quiz=q3, texto_pregunta="Para las composiciones festivas ecuatorianas desarrolladas en Loja en el siglo XX, ¿qué género compitió con el pasillo por sonar en las radios?")
    Opcion.objects.create(pregunta=p3_9, texto="El bolero romántico y caribeño", es_correcta=True)
    Opcion.objects.create(pregunta=p3_9, texto="La sonata escocesa", es_correcta=False)
    Opcion.objects.create(pregunta=p3_9, texto="El punk", es_correcta=False)

    p3_10 = Pregunta.objects.create(quiz=q3, texto_pregunta="En la actualidad (Siglo XXI), la música patrimonial lojana está atravesando experimentalmente por:")
    Opcion.objects.create(pregunta=p3_10, texto="Una decadencia total de su uso", es_correcta=False)
    Opcion.objects.create(pregunta=p3_10, texto="Obligación del Estado de jamás ser modificada", es_correcta=False)
    Opcion.objects.create(pregunta=p3_10, texto="Procesos de innovación, fusiones con jazz/pop/rock y digitalización internacional", es_correcta=True)

    print("Success: Base de datos recreada con exitosamente 3 Quizzes, midiendo 10 preguntas por cada cuestionario. Total de 30 preguntas creadas.")

if __name__ == '__main__':
    populate()
