from .default import *  # noqa
import dj_database_url
from getenv import env

# ##############################################################################
# remove before flight
# ##############################################################################
raise Exception('Production not yet configured.')

# ===================
# = Global Settings =
# ===================

UNIQUE_PREFIX = '{{ cookiecutter.project_name }}_production'
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# ===================
# = Server Settings =
# ===================

DEPLOYMENT = {
    'git_repository': 'git@github.com:{{ cookiecutter.repo_organisation }}/{{ cookiecutter.repo_name }}.git',
    'git_branch': 'master',
    'git_remote': 'origin',
    'hosts': ['.nine.ch'],
    'user': 'www-data',
    'project': '{{ cookiecutter.repo_name }}',
    'root': '/home/www-data/projects',
    'is_stage': False,
}

DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['CONN_MAX_AGE'] = 60

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'KEY_PREFIX': UNIQUE_PREFIX,
        'VERSION': 1,
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        },
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

RAVEN_CONFIG = {
    'dsn': '',
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# ===========================
# = Django-specific Modules =
# ===========================

MIDDLEWARE_CLASSES += ('allink_essentials.middleware.validate_host_middleware.ValidateHostMiddleware',)

# ==========
# = Celery =
# ==========

BROKER_URL = env('BROKER_URL', None)
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', "redis://localhost/0")
CELERYD_CONCURRENCY = env('CELERYD_CONCURRENCY', 1)
CELERY_SEND_EVENTS = False
CELERY_ENABLE_UTC = True

# load celery
if BROKER_URL:
    import djcelery
    djcelery.setup_loader()
