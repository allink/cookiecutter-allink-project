from .default import *  # noqa

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
