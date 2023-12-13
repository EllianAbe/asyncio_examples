# create a stopwatch decorator
from datetime import datetime
import inspect


def stopwatch(func):
    """
    A decorator function that measures the duration of the decorated function.

    Parameters:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    """
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Duration in module {func.__module__}: ', end - start)
        return result
    return wrapper
