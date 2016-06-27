# from __future__ import absolute_import
# from getenv import env
# import dotenv

# import os

# from celery import Celery

# dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', "%s" % env('DJANGO_SETTINGS_MODULE', ''))

# from django.conf import settings  # noqa

# app = Celery('{{cookiecutter.project_name}}')
# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# Uncomment if celery is used
