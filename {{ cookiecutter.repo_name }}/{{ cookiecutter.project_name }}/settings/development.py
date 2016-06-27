from .default import *  # noqa
# import djcelery

import os

# ===================
# = Global Settings =
# ===================

DEBUG = True

# ===================
# = Server Settings =
# ===================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FILE_STORAGE = 'allink_essentials.storage.ascii_file_system_storage.ASCIIFileSystemStorage'
CELERY_RESULT_PERSISTENT = False

# ================
# = File serving =
# ================

STATIC_ROOT = os.path.join(BASE_DIR, 'compiled_static')

# =====================
# = Pipeline settings =
# =====================

PIPELINE['LESS_ARGUMENTS'] = '--line-numbers=\'comments\''

# load celery
# djcelery.setup_loader()
