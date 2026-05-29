from functools import wraps


def log_action(action: str):
    def result_action(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)

            if result and "id" in result:
                print(f"{action} action successful, ID: {str(result['id'])}")

            return result

        return wrapper

    return result_action
