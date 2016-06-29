import os
import re
from getenv import env
import dj_database_url
import django_cache_url
# from celery.task.schedules import crontab

# ===================
# = Global Settings =
# ===================

ADMINS = (
    ('itcrowd', 'itcrowd@allink.ch'),
)
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ["*"]
LANGUAGE_CODE = 'de'
LANGUAGES = (
    ('de', 'German'),
    # ('en', 'English'),
    # ('fr', 'French'),
)
TIME_ZONE = 'Europe/Zurich'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
ATOMIC_REQUESTS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# ===============================
# = Databases, Caches, Sessions =
# ===============================

DATABASES = {'default': dj_database_url.config()}

CACHES = {
    'default': django_cache_url.config(),
    'sessions': django_cache_url.config(env="SESSION_CACHE_URL"),
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'sessions'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
SESSION_COOKIE_HTTPONLY = True

# ===========================
# = Directory Declaractions =
# ===========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# ================
# = File serving =
# ================

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '{{ cookiecutter.project_name }}', 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'allink_essentials.storage.lossless_image_compress_storage.LosslessImageCompressStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# ===========================
# = Django-specific Modules =
# ===========================

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1']

# =============
# = Templates =
# =============

CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'universe.context_processors.config',
    'universe.context_processors.sortable_menu',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': False,
        'DIRS': [os.path.join(BASE_DIR, 'meinau', 'templates')],
        'OPTIONS': {
            'debug': True,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'context_processors': CONTEXT_PROCESSORS
        }
    },
]

# ===============
# = Django Apps =
# ===============

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'feincms',
    'feincms.module.page',
    'allink_essentials',
    'allink_essentials.in_footer',
    'mptt',
    'robots',
    'allink_essentials.analytics',
    'debug_toolbar',
    'raven.contrib.django.raven_compat',
    'admin_sso',
    'sorl.thumbnail',
    'solo.apps.SoloAppConfig',
    'webpack_loader',
    # 'djcelery',
    '{{ cookiecutter.project_name }}',
)

MIGRATION_MODULES = {
    'page': '{{ cookiecutter.project_name }}.migrations_page',
}

# ===========
# = Logging =
# ===========

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'skip_unreadable_posts': {
            '()': 'allink_essentials.logging.filters.SkipUnreadablePostError',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'filters': ['require_debug_false', 'skip_unreadable_posts'],
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

# ====================
# = FeinCMS settings =
# ====================

FEINCMS_ADMIN_MEDIA = '/static/feincms/'
FEINCMS_TINYMCE_INIT_CONTEXT = {
    'TINYMCE_JS_URL': os.path.join(STATIC_URL, 'lib/tinymce/tinymce.min.js'),
    'TINYMCE_LINK_LIST_URL': '/admin/tiny_mce_links.js',
    'TINYMCE_EXTERNAL_IMAGE_LIST_URL': None
}
FEINCMS_RICHTEXT_INIT_CONTEXT = FEINCMS_TINYMCE_INIT_CONTEXT
FEINCMS_RICHTEXT_INIT_TEMPLATE = 'admin/tinymce_config.html'

# ==========
# = Celery =
# ==========

CELERYBEAT_SCHEDULE = {
    # 'eaxample-print': {
    #     'task': 'tasks.print',
    #     'schedule': timedelta(seconds=30)
    # },
    # 'detect_overdue_invoices': {
    #     'task': 'oscar_apps.order.tasks.invoice_overdue_task',
    #     'schedule': crontab(hour=3, minute=13),
    # },
}

BROKER_URL = env('BROKER_URL', None)
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', 'rpc://')
CELERYD_CONCURRENCY = env('CELERYD_CONCURRENCY', 1)
CELERY_SEND_EVENTS = False
CELERY_ENABLE_UTC = True

# ==========================
# = Miscellaneous Settings =
# ==========================

DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID = env('DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID', None)
DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET = env('DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET', None)

THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2]

# GOOGLE_ANALYTICS_ID = ""
GOOGLE_TAG_MANAGER_ID = ""

IGNORABLE_404_URLS = (
    re.compile(r'^/cgi-bin/'),
    re.compile(r'\.php$'),
    re.compile(r'\.pl$'),
    re.compile(r'\.cgi$'),
)

AUTHENTICATION_BACKENDS = (
    'admin_sso.auth.DjangoSSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)
