from .default import *  # noqa

# ===================
# = Global Settings =
# ==================

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# ===================
# = Server Settings =
# ===================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travisci',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'KEY_PREFIX': 'travisci',
        'VERSION': 1,
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        },
    },
}

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# ===============
# = Django Apps =
# ===============

INSTALLED_APPS = INSTALLED_APPS + ('django.contrib.sessions',)  # without this django test client crashes

# =======================
# = Compressor settings =
# =======================

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
