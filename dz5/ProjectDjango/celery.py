import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dz5.ProjectDjango.settings')

app = Celery()
app.config_from_object('django.conf:settings', namespace='CELERY')



@app.task
def test_task():
    return 2 + 2