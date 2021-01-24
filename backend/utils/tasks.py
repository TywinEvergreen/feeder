from django.core import management

from feeder.celery import app


@app.task
def cleanup_unused_files():
    """
    Очищает неисползуемые файлы
    """
    management.call_command('cleanup_unused_media', '--noinput')
