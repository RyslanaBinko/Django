import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectDjango.settings')

app = Celery("Django")
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task(bind=True)
def test_task(self):
    return 2 + 2
