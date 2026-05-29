def log_result_decorator(func):
    def wrapper(*args):
        result = func(*args)

        print(result)
        return result

    return wrapper
