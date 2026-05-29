def log_all_decorator(func):
    def wrapper(*args):
        result = func(*args)
        if result:
            for i in result:
                print(result[i])
        else:
            print("no rows")

        return result

    return wrapper
