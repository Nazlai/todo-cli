def log_action_decorator(action: str):
    def result_action(func):
        def wrapper(*args):
            result = func(*args)

            if result and "id" in result:
                print(f"{action} action successful, ID: {str(result['id'])}")

                return result

        return wrapper

    return result_action
