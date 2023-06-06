# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cpu.settings")
app = Celery("cpu")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()