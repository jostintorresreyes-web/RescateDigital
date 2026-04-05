import os
import re
import polib

templates_dir = 'templates'

trans_re = re.compile(r'{%\s*trans\s+[\'"](.*?)[\'"]\s*%}')
blocktrans_re = re.compile(r'{%\s*blocktrans\s*%}(.*?){%\s*endblocktrans\s*%}', re.DOTALL)

strings = set()

for root, dirs, files in os.walk(templates_dir):
    for f in files:
        if f.endswith('.html'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                content = file.read()
                for match in trans_re.findall(content):
                    strings.add(match)
                for match in blocktrans_re.findall(content):
                    strings.add(match.strip())

translations_en = {
    "Inicio": "Home",
    "Historia musical": "Musical History",
    "Artistas": "Artists",
    "Juegos": "Games",
    "Sobre el proyecto": "About the Project",
    "Cerrar Sesión": "Logout",
    "Login": "Login",
    "Navegación": "Navigation",
    "Historia Musical": "Musical History",
    "Archivo Digital": "Digital Archive",
    "Institucional": "Institutional",
    "Sobre el Proyecto": "About the Project",
    "Investigadores": "Researchers",
    "Alianzas": "Alliances",
    "Contacto": "Contact",
    "Explorar Archivo": "Explore Archive",
    "Conocer el Proyecto": "Know the Project",
    "Acerca de la Plataforma": "About the Platform",
    "Curiosidad": "Curiosity",
    "Archivo Vivo": "Living Archive",
    "Capital Musical": "Musical Capital",
    "Únete": "Join",
    "Aprende Jugando": "Learn by Playing",
    "Quiz Musical": "Musical Quiz",
    "Jugar ahora": "Play now",
    "Sistema de Puntos": "Point System",
    "Ver ranking": "View ranking",
    "Línea del Tiempo Musical": "Musical Timeline",
    "Explorar la Cronología": "Explore the Chronology",
    "Biografía": "Biography",
    "Composiciones": "Compositions",
    "Legado Cultural": "Cultural Heritage",
    "¿Cuánto sabes de {{ nombre }}?": "How much do you know about {{ nombre }}?",
    "Empezar Quiz": "Start Quiz",
    "Volver a la selección de juegos": "Back to game selection",
    "Enviar Respuestas": "Submit Answers",
    "Preguntas": "Questions",
    "Posibles Puntos": "Possible Points",
    "Respondido": "Answered",
    "Comenzar Reto": "Start Challenge",
    "No hay quizzes disponibles aún.": "There are no quizzes available yet.",
    "Pronto prepararemos nuevos desafíos musicales para ti.": "We will soon prepare new musical challenges for you.",
    "Ver Ranking": "View Ranking",
    "Directorio de Artistas Lojanos": "Loja Artists Directory",
    "Conoce a los músicos y compositores que han marcado la historia cultural de Loja.": "Meet the musicians and composers who have marked the cultural history of Loja.",
    "No se encontraron artistas registrados.": "No registered artists found.",
    "Historia Musical de Loja - Rescate Digital": "Musical History of Loja - Digital Rescue",
    "Línea de tiempo de la música lojana": "Loja Music Timeline",
    "Viaja a través de los siglos y descubre cómo Loja se convirtió en el epicentro sonoro del Ecuador. Explora nuestra historia mediante esta línea de tiempo interactiva.": "Travel through the centuries and discover how Loja became the sonic epicenter of Ecuador. Explore our history through this interactive timeline.",
    "Siglos XVI–XVIII": "16th–18th Centuries",
    "Orígenes coloniales": "Colonial Origins",
    "Con la colonización española se introducen formas musicales europeas.": "With Spanish colonization, European musical forms were introduced.",
    "Llegan instrumentos como la guitarra, el arpa y el violín.": "Instruments like the guitar, harp, and violin arrive.",
    "Se produce una fusión entre música indígena y europea, dando origen a expresiones mestizas.": "A fusion between indigenous and European music occurred, originating mestizo expressions.",
    "La música se desarrolla principalmente en contextos religiosos y festividades.": "Music developed mainly in religious contexts and festivities.",
    "Siglo XIX": "19th Century",
    "Formación de identidad musical": "Formation of Musical Identity",
    "Loja comienza a consolidarse como un centro cultural importante en el sur del Ecuador.": "Loja begins to consolidate as an important cultural center in southern Ecuador.",
    "Se adoptan géneros como el pasillo, el vals y el pasacalle.": "Genres like pasillo, waltz, and pasacalle were adopted.",
    "Surgen músicos locales que desarrollan estilos propios.": "Local musicians emerge developing their own styles.",
    "La música pasa a formar parte de la vida cotidiana y social.": "Music became part of daily and social life.",
    "Finales s. XIX – Inicios s. XX": "Late 19th - Early 20th Centuries",
    "Auge del pasillo lojano": "Rise of the Loja Pasillo",
    "El pasillo se convierte en el género predominante en la región.": "The pasillo becomes the predominant genre in the region.",
    "Se define un estilo lojano caracterizado por su tono melancólico y poético.": "A Loja style is defined, characterized by its melancholic and poetic tone.",
    "Se popularizan las serenatas y el uso de la guitarra.": "Serenades and the use of the guitar become popular.",
    "Destacan compositores como Salvador Bustamante Celi y Segundo Cueva Celi.": "Composers like Salvador Bustamante Celi and Segundo Cueva Celi stand out.",
    "Décadas de 1920–1950": "1920s–1950s",
    "Consolidación y reconocimiento": "Consolidation and Recognition",
    "Loja es reconocida como la 'Capital Musical del Ecuador'.": "Loja is recognized as the 'Musical Capital of Ecuador'.",
    "Se fortalece la educación musical y se crea el Conservatorio Salvador Bustamante Celi.": "Musical education is strengthened, and the Salvador Bustamante Celi Conservatory is created.",
    "El pasillo lojano se difunde a nivel nacional.": "The Loja pasillo spreads nationally.",
    "Influyen también figuras como Carlos Rubira Infante y Nicasio Safadi.": "Figures like Carlos Rubira Infante and Nicasio Safadi also influence.",
    "Décadas de 1960–1980": "1960s–1980s",
    "Expansión y modernización": "Expansion and Modernization",
    "La radio y las grabaciones permiten una mayor difusión.": "Radio and recordings allow for greater dissemination.",
    "Se incorporan nuevos arreglos musicales y estilos.": "New musical arrangements and styles are incorporated.",
    "El pasillo convive con otros géneros como el bolero.": "The pasillo coexists with other genres like bolero.",
    "Se forman tríos y agrupaciones musicales representativas.": "Representative trios and musical groups are formed.",
    "Décadas de 1990–2000": "1990s–2000s",
    "Preservación y nuevas generaciones": "Preservation and New Generations",
    "Se intensifican los esfuerzos por conservar la música tradicional.": "Efforts to preserve traditional music intensify.",
    "Se fortalece la formación académica musical.": "Academic musical training is strengthened.",
    "Nuevas generaciones reinterpretan el pasillo lojano.": "New generations reinterpret the Loja pasillo.",
    "Se organizan festivales culturales para promover la identidad musical.": "Cultural festivals are organized to promote musical identity.",
    "Siglo XXI (2000–actualidad)": "21st Century (2000–Present)",
    "Innovación y proyección": "Innovation and Projection",
    "Fusión del pasillo con géneros modernos como jazz, pop y rock.": "Fusion of pasillo with modern genres like jazz, pop, and rock.",
    "Uso de plataformas digitales para difusión internacional.": "Use of digital platforms for international dissemination.",
    "Revalorización del pasillo como patrimonio cultural.": "Revaluation of the pasillo as cultural heritage.",
    "Surgen artistas que combinan tradición e innovación.": "Artists emerge combining tradition and innovation.",
    "Características principales de la música lojana": "Main Characteristics of Loja Music",
    "Predominio del pasillo lojano.": "Predominance of the Loja pasillo.",
    "Uso de guitarra, requinto y voz.": "Use of guitar, requinto, and voice.",
    "Letras románticas, nostálgicas y poéticas.": "Romantic, nostalgic, and poetic lyrics.",
    "Fuerte identidad cultural regional.": "Strong regional cultural identity.",
    "Iniciar Sesión - Rescate Digital": "Login - Digital Rescue",
    "Bienvenido": "Welcome",
    "Ingresa a tu cuenta para continuar explorando": "Log in to your account to continue exploring",
    "Correo Electrónico": "Email Address",
    "Contraseña": "Password",
    "¿Olvidaste tu contraseña?": "Forgot your password?",
    "Ingresar": "Login",
    "¿No tienes una cuenta?": "Don't have an account?",
    "Regístrate gratis": "Sign up for free",
    "tu@correo.com": "you@email.com",
    "Registro - Rescate Digital": "Registration - Digital Rescue",
    "Únete a la plataforma": "Join the platform",
    "Crea una cuenta para jugar y aprender sobre la música lojana.": "Create an account to play and learn about Loja's music.",
    "Nombre completo o Apodo": "Full Name or Nickname",
    "Ej: Juan Pérez": "Ex: John Doe",
    "Crea una contraseña segura": "Create a secure password",
    "Confirmar Contraseña": "Confirm Password",
    "Repite tu contraseña": "Repeat your password",
    "Registrar Cuenta": "Register Account",
    "¿Ya tienes una cuenta?": "Already have an account?",
    "Inicia sesión aquí": "Login here",
    "RESCATE DIGITAL": "DIGITAL RESCUE",
    "Músico y Compositor": "Musician and Composer",
    "Un proyecto destinado a la recuperación, digitalización y puesta en valor del patrimonio musical de la ciudad de Loja, Ecuador.": "A project aimed at the recovery, digitization, and enhancement of the musical heritage of the city of Loja, Ecuador.",
    "Rescate Digital de la Historia Musical Lojanauador.": "Un projet destiné à la récupération, à la numérisation et à la mise en valeur du patrimoine musical de la ville de Loja, en Équateur.",
    "Rescate Digital de la Historia Musical Lojana. Todos los derechos reservados.": "Sauvetage numérique de l'histoire musicale de Loja. Tous droits réservés."
}

def build_po(lang_code, lang_name, trans_dict):
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': '2023-01-01 12:00+0000',
        'PO-Revision-Date': '2023-01-01 12:00+0000',
        'Last-Translator': 'you <you@example.com>',
        'Language-Team': f'{lang_name} <yourteam@example.com>',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
        'Language': lang_code
    }
    
    for string in strings:
        entry = polib.POEntry(
            msgid=string,
            msgstr=trans_dict.get(string, string)
        )
        po.append(entry)
        
    os.makedirs(f'locale/{lang_code}/LC_MESSAGES', exist_ok=True)
    po.save(f'locale/{lang_code}/LC_MESSAGES/django.po')
    po.save_as_mofile(f'locale/{lang_code}/LC_MESSAGES/django.mo')

build_po('en', 'English', translations_en)
print("Translations built successfully!")
