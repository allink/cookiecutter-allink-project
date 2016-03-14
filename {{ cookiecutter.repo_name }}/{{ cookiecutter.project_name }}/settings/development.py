from .default import *  # noqa

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

# ================
# = File serving =
# ================

STATIC_ROOT = os.path.join(BASE_DIR, 'compiled_static')
