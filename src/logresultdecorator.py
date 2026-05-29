from functools import wraps


def log_result(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)

        print(result)
        return result

    return wrapper
