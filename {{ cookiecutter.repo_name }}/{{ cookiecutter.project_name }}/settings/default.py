import os
import re
from getenv import env
import dj_database_url
import django_cache_url

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
    ('en', 'English'),
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
    'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# ===========================
# = Django-specific Modules =
# ===========================

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
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

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '{{ cookiecutter.project_name }}', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

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
    'pipeline',
    'mptt',
    'robots',
    'allink_essentials.analytics',
    'debug_toolbar',
    'raven.contrib.django',
    'admin_sso',
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
            'class': 'raven.contrib.django.handlers.SentryHandler',
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

# =====================
# = Pipeline settings =
# =====================


PIPELINE = {
    'PIPELINE_ENABLED': False,
    'JAVASCRIPT': {
        'main': {
            'source_filenames': (
                'lib/jquery-1.11.0.js',
                'lib/jquery.sticky.js',
                'lib/bootstrap/js/transition.js',
                'lib/bootstrap/js/dropdown.js',
                'lib/bootstrap/js/collapse.js',
                'javascript/main.js',
            ),
            'output_filename': 'js/main.js',
        },
        'ie9': {
            'source_filenames': (
                'lib/jquery.placeholder.js',
                'javascript/ie9.js',
            ),
            'output_filename': 'js/ie9.js',
        },
    },
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
                'icomoon/style.css',
                'lib/slick/slick.css',
                'stylesheets/base.less',
            ),
            'output_filename': 'css/main.css',
            'variant': 'datauri',
        },
    },
    'COMPILERS': (
        'pipeline.compilers.less.LessCompiler',
    ),
    'LESS_BINARY': os.path.join(BASE_DIR, 'node_modules', '.bin', 'lessc'),
    'CSS_COMPRESSOR': 'pipeline.compressors.cssmin.CSSMinCompressor',
    'CSSMIN_BINARY': os.path.join(BASE_DIR, 'node_modules', '.bin', 'cssmin'),
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
    'UGLIFYJS_BINARY': os.path.join(BASE_DIR, 'node_modules', '.bin', 'uglifyjs'),
}

# ==========
# = Celery =
# ==========

CELERYBEAT_SCHEDULE = {
    # 'eaxample-print': {
    #     'task': 'tasks.print',
    #     'schedule': timedelta(seconds=30)
    # },
}

BROKER_URL = env('BROKER_URL', None)
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', None)
CELERYD_CONCURRENCY = env('CELERYD_CONCURRENCY', 1)
CELERY_SEND_EVENTS = False
CELERY_ENABLE_UTC = True

# ==========================
# = Miscellaneous Settings =
# ==========================

DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID = env('DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID', None)
DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET = env('DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET', None)

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
