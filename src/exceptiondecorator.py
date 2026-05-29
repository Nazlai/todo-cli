def log_exception(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            if hasattr(e, "message"):
                print(e.message)
            else:
                print("an error occurred")

    return wrapper
