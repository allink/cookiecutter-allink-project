from .default import *  # noqa
from getenv import env

# ===================
# = Global Settings =
# ===================

UNIQUE_PREFIX = '{{ cookiecutter.project_name }}'
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# ===================
# = Server Settings =
# ===================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': UNIQUE_PREFIX,
        'USER': env('PG_USER'),
        'PASSWORD': env('PG_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FILE_STORAGE = 'allink_essentials.storage.ascii_file_system_storage.ASCIIFileSystemStorage'

# ===============
# = Django Apps =
# ===============

INSTALLED_APPS = INSTALLED_APPS + ('django.contrib.sessions',)
