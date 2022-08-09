from functools import wraps


def log(function):
    @wraps(function)
    def wrapped(**kwargs):
        print(f"Calling {function.__name__} with {kwargs}")
        result = function(**kwargs)
        print(f"Result is {result}")
        return result
    return wrapped
