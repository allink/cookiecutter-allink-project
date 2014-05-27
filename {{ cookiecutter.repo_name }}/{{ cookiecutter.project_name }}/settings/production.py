from .default import *  # noqa

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
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

# ===========================
# = Django-specific Modules =
# ===========================

MIDDLEWARE_CLASSES += ('allink_essentials.middleware.validate_host_middleware.ValidateHostMiddleware',)
