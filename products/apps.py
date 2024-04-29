from django.apps import AppConfig

# For FB Messenger messages with APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        from .tasks import send_facebook_message
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            send_facebook_message,
            trigger=IntervalTrigger(hours=3),  # Adjust the interval as needed
            id='send_fb_message_every_3_hours',
            replace_existing=True)
        scheduler.start()