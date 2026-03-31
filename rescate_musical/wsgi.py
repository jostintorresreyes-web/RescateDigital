"""
WSGI config for rescate_musical project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')

application = get_wsgi_application()

# Vercel necesita que el objeto WSGI se llame 'app'
app = application
