def log_result(func):
    def wrapper(*args):
        result = func(*args)

        print(result)
        return result

    return wrapper
