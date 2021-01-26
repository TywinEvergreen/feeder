# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
import importlib.util
from .celery import app as celery_app

__all__ = ('celery_app',)

mypy_package = importlib.util.find_spec("mypy")
if mypy_package:
    from .checks import mypy
