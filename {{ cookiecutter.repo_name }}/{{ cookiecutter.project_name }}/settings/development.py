from .default import *  # noqa

# ===================
# = Global Settings =
# ===================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# ===================
# = Server Settings =
# ===================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FILE_STORAGE = 'allink_essentials.storage.ascii_file_system_storage.ASCIIFileSystemStorage'

# ===============
# = Django Apps =
# ===============

INSTALLED_APPS = INSTALLED_APPS + ('django.contrib.sessions',)
