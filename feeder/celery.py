import os
from django.utils import timezone

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feeder.settings')

app = Celery('feeder')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-new-albums': {
        'task': 'spotify.tasks.get_new_albums',
<<<<<<< HEAD
        'schedule': timezone.timedelta(seconds=30)  # TODO: Поставить 12 часов
    },
    'get-new-videos': {
        'task': 'youtube.tasks.get_new_videos',
        'schedule': timezone.timedelta(seconds=30)  # TODO: Поставить 1 час
    },
    'cleanup-unused-media': {
        'task': 'utils.tasks.cleanup_unused_media',
        'schedule': timezone.timedelta(seconds=30)  # TODO: Поставить 1 час
=======
        'schedule': timezone.timedelta(hours=1)
    },
    'get-new-videos': {
        'task': 'youtube.tasks.get_new_videos',
        'schedule': timezone.timedelta(hours=1)
    },
    'cleanup-unused-media': {
        'task': 'utils.tasks.cleanup_unused_media',
        'schedule': timezone.timedelta(hours=6)
>>>>>>> 7f3a02d06ac6fb30f6465bf0cdc13b7ea96cf8ae
    }
}
