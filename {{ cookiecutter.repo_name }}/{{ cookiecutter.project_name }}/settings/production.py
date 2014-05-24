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

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# ===================
# = Server Settings =
# ===================

DATABASES['default']['CONN_MAX_AGE'] = 60

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
