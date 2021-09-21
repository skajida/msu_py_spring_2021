from functools import wraps
from signal import setitimer, signal, ITIMER_REAL, SIGALRM


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def handler(signum, frame):
    raise TimeoutException('Timed out')


class Handler:

    def __init__(self, seconds):
        self.seconds = seconds

    def __enter__(self):
        self.prev_handler = signal(SIGALRM, handler)
        setitimer(ITIMER_REAL, self.seconds)

    def __exit__(self, exc_type, exc_value, traceback):
        signal(SIGALRM, self.prev_handler)
        setitimer(ITIMER_REAL, 0)


def timeout(seconds):
    def decorator(func):
        if not isinstance(seconds, (int, float)) or seconds <= 0:
            return func

        @wraps(func)
        def wrapper(*args, **kwargs):
            with Handler(seconds):
                return func(*args, **kwargs)
        return wrapper
    return decorator
