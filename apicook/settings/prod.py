# Database configuration	
from .settings import *	
import os	

DEBUG = True	
TEMPLATE_DEBUG = DEBUG	

# Database configuration	
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bean3330_musicschool',
        'USER': 'bean3330_gabaanbe4493',
        'PASSWORD': 'AzeGabaanbe4493!3944',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

BASE_DIR = '/home/bean3330/django/musicschool/'
SECRET_KEY = '74p9xvv=)91x@v$zs2xrijol3o#u0)ez7ozt1aszz8qx9@u^^s'

ALLOWED_HOSTS = ['espace.bean3330.odns.fr', 'espace.lecoledemusiquesactuelles.fr']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ADMINS = (
    ('adminbean44880', '44880adminbean44880'),
)

# Managers configuration
MANAGERS = ADMINS

STATIC_URL = '/static/'
BASE_PUBLIC = '/home/bean3330/public_html/'
STATIC_ROOT = os.path.join(BASE_PUBLIC, 'static')

STATIC_DIRS  = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/' 
