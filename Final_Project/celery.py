from __future__ import absolute_import, unicode_literals
import os
from celery import Celery



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final_Project.settings')
page_access_token = os.environ.get('FACEBOOK_PAGE_ACCESS_TOKEN')



app = Celery('Final_Project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
