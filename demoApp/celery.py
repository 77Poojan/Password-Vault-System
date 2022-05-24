import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoApp.settings')

app = Celery('demoApp')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(timezone = 'Asia/Kathmandu')
app.conf.enable_utc = False

#Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-perodically': {
        'task': 'api.tasks.send_mail_task',
        'schedule': crontab(hour=17,minute=25),  
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')