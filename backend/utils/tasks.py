from django.core import management

from feeder.celery import app


@app.task
def cleanup_unused_media():
    """
    Очищает неисползуемые файлы
    """
    management.call_command('cleanup_unused_media', '--noinput')
