from functools import wraps

# Decorator function
# def log(function):
#     @wraps(function)
#     def wrapped(**kwargs):
#         print(f"\n\nFunction: {function.__name__}")
#         print("\nParams:")
#         for k, v in kwargs.items():
#             print(f"{k}: {v}")
#         result = function(**kwargs)
#         print(f"\nResult: {result}")
#         return result
#     return wrapped


# Decorator object
class log:
    
    index = 0

    @staticmethod
    def __call__(function):
        @wraps(function)
        def wrapped(**kwargs):
            log.index += 1
            print(f"\nTest {log.index}")
            print(f"Function: {function.__name__}")
            print("Params:")
            for k, v in kwargs.items():
                print(f"\t{k}: {v}")
            result = function(**kwargs)
            print(f"Result: {result}")
            return result
        return wrapped
