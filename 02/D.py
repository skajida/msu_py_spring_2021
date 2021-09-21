from functools import wraps


def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper._current_depth == 0:
            wrapper.rdepth = 0
            wrapper.ncalls = 0
        wrapper._current_depth += 1
        wrapper.rdepth = max(wrapper.rdepth, wrapper._current_depth)
        wrapper.ncalls += 1
        res = func(*args, **kwargs)
        wrapper._current_depth -= 1
        return res
    wrapper._current_depth = 0
    return wrapper
