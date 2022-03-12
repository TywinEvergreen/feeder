import inspect

from django.utils.module_loading import import_string


def signal_decorator(path):
    """
    Imports signal by given path into the function
    """

    def inner(func):
        def wrapper(*args, **kwargs):
            signal = import_string(path)

            # Proceed only if imported signal takes all parameters needed
            signal_parameters = ["sender", "instance", "created", "kwargs"]

            if all(
                arg in inspect.signature(signal).parameters for arg in signal_parameters
            ):
                func(*args, **kwargs)
            else:
                raise RuntimeError(
                    """
                    Passed function does not take all parameters needed: 
                    sender, instance, created, kwargs. 
                    Are you sure passed function is a signal?
                    """
                )

        return wrapper

    return inner
