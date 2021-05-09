from django.utils.module_loading import import_string


def signal_decorator(func):
    """
    Imports signal by given path into the function
    """
    def wrapper(*args, **kwargs):
        print("qwerty")
        # import_string('youtube.signals.create_video_notifications')
        func(*args, **kwargs)

    return wrapper
