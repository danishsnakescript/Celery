from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery_core.settings')

app = Celery('Celery_core')
    
app.config_from_object('django.conf:settings', namespace='CELERY')
    
  # Load task modules from all registered Django apps.
app.autodiscover_tasks()
    
    
app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')