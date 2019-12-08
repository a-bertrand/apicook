"""
WSGI config for apicook project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.getenv('ENVRONMENT_KEY') == "PROD":
    settings = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apicook.settings.prod")
else:
    settings = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apicook.settings.dev")

application = get_wsgi_application()
