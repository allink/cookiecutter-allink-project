from .default import *  # noqa

import os

# ===================
# = Global Settings =
# ===================

DEBUG = True
THUMBNAIL_DEBUG = True

# ===================
# = Server Settings =
# ===================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FILE_STORAGE = 'allink_essentials.storage.ascii_file_system_storage.ASCIIFileSystemStorage'

# ================
# = File serving =
# ================

STATIC_ROOT = os.path.join(BASE_DIR, 'compiled_static')

# ===========
# = Webpack =
# ===========

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,
        'BUNDLE_DIR_NAME': 'build/',
        'STATS_FILE': os.path.join(BASE_DIR, '{{cookiecutter.project_name}}', 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}
