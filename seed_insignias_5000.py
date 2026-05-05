import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Cromo

def seed():
    insignias = [
        {"nombre": "Estrella del Sur", "desc": "Otorgada a los músicos prometedores.", "puntos": 600, "icono": "fas fa-star", "rareza": "Rara", "color": "#3498db"},
        {"nombre": "Melodía Andina", "desc": "Refleja el alma de la cordillera.", "puntos": 700, "icono": "fas fa-mountain", "rareza": "Rara", "color": "#3498db"},
        {"nombre": "El Compás Perdido", "desc": "Un antiguo ritmo hallado en las partituras olvidadas.", "puntos": 800, "icono": "fas fa-shoe-prints", "rareza": "Épica", "color": "#9b59b6"},
        {"nombre": "Acordes de Pasillo", "desc": "Para aquellos que entienden la nostalgia lojana.", "puntos": 1000, "icono": "fas fa-heart", "rareza": "Épica", "color": "#9b59b6"},
        {"nombre": "Baston de Director", "desc": "El liderazgo y control de la orquesta sinfónica.", "puntos": 1200, "icono": "fas fa-magic", "rareza": "Épica", "color": "#9b59b6"},
        {"nombre": "Lira de Oro", "desc": "Instrumento mítico tocado por los juglares legendarios.", "puntos": 1500, "icono": "fas fa-harp", "rareza": "Legendaria", "color": "#f39c12"},
        {"nombre": "Voz de la Catedral", "desc": "Una voz que resuena en toda la plaza central de Loja.", "puntos": 1800, "icono": "fas fa-church", "rareza": "Legendaria", "color": "#f39c12"},
        {"nombre": "Piano de Cola Imperial", "desc": "Majestuosidad en cada tecla blanca y negra.", "puntos": 2000, "icono": "fas fa-ring", "rareza": "Legendaria", "color": "#e67e22"},
        {"nombre": "Sinfonía Inmortal", "desc": "Una obra maestra que perdura a través de los siglos.", "puntos": 2500, "icono": "fas fa-infinity", "rareza": "Mítica", "color": "#e74c3c"},
        {"nombre": "Corona de Laurel Musical", "desc": "El máximo honor otorgado en el festival de la música.", "puntos": 3000, "icono": "fas fa-leaf", "rareza": "Mítica", "color": "#e74c3c"},
        {"nombre": "Astro de Loja", "desc": "Brilla con luz propia en el firmamento musical.", "puntos": 3500, "icono": "fas fa-star-of-life", "rareza": "Mítica", "color": "#e74c3c"},
        {"nombre": "Alma del Maestro", "desc": "La sabiduría y experiencia de todos los compositores lojanos.", "puntos": 4000, "icono": "fas fa-brain", "rareza": "Suprema", "color": "#00ffcc"},
        {"nombre": "Leyenda Viva", "desc": "Te has convertido en una leyenda de la música nacional.", "puntos": 4500, "icono": "fas fa-fire-alt", "rareza": "Suprema", "color": "#00ffcc"},
        {"nombre": "Guardián del Patrimonio", "desc": "El protector definitivo del rescate musical lojano.", "puntos": 5000, "icono": "fas fa-shield-alt", "rareza": "Suprema", "color": "#00ffcc"}
    ]

    for c in insignias:
        obj, created = Cromo.objects.get_or_create(
            nombre=c["nombre"],
            defaults={
                "nombre_en": c["nombre"],
                "descripcion": c["desc"],
                "descripcion_en": c["desc"],
                "puntos_requeridos": c["puntos"],
                "icono": c["icono"],
                "rareza": c["rareza"],
                "color_borde": c["color"]
            }
        )
        if created:
            print(f"Insignia añadida: {c['nombre']} ({c['puntos']} pts)")
        else:
            print(f"Insignia existente: {c['nombre']} ({c['puntos']} pts)")

if __name__ == '__main__':
    seed()
    print("¡Expansión de Insignias hasta 5000 completada exitosamente!")
