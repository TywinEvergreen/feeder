import os
import shutil

from django.test.runner import DiscoverRunner

from feeder.settings import MEDIA_ROOT


class CustomTestRunner(DiscoverRunner):
    """
    Тестировщик удаляет директорию
    media/testing после выполнения тестов
    """

    def teardown_test_environment(self, *args, **kwargs):
        if os.path.isdir(os.path.join(MEDIA_ROOT, 'testing')):
            shutil.rmtree(os.path.join(MEDIA_ROOT, 'testing'))
        super(CustomTestRunner, self).teardown_test_environment(*args, **kwargs)
