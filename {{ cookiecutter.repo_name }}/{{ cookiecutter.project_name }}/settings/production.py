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
    'dsn': '{{ cookiecutter.sentry_dsn}}',
}

CACHES = {
    'default': {
        'OPTIONS': {
            "PARSER_CLASS": "redis.connection.HiredisParser",
        },
        'LOCATION': '127.0.0.1:6379:1',
        'KEY_PREFIX': '{{ cookiecutter.project_name }}_production',
        'BACKEND': 'django_redis.cache.RedisCache'
    },
    'sessions': {
        'OPTIONS': {
            "PARSER_CLASS": "redis.connection.HiredisParser",
        },
        'LOCATION': '127.0.0.1:6379:2',
        'KEY_PREFIX': '{{ cookiecutter.project_name }}_production',
        'BACKEND': 'django_redis.cache.RedisCache'
    }
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

# ===========================
# = Django-specific Modules =
# ===========================

MIDDLEWARE_CLASSES += ['allink_essentials.middleware.validate_host_middleware.ValidateHostMiddleware']
