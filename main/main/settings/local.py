from .base import *

SECRET_KEY = 'django-insecure-pb^zju77ymt(4$q)zgd7^l%iwj2!ke@z*--v1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}