from .base import INSTALLED_APPS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pygameWorkshopRegistration',
        'USER': 'shashank',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
