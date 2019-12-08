import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'apicook.settings.prod'
application = get_wsgi_application()
