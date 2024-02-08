import time

# Timer Decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Time taken for {func.__name__}: {duration} seconds")
        return result
    return wrapper

# Memoization Decorator
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


# Authorization Decorator
class UnauthorizedError(Exception):
    pass

def authorize(username, password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if username == "admin" and password == "password":
                return func(*args, **kwargs)
            else:
                raise UnauthorizedError("Unauthorized access")
        return wrapper
    return decorator



# Example usage:

@timer
def some_function():
    time.sleep(2)
    print("Function executed")

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@authorize("admin", "password")
def secret_function():
    print("Authorized access")

if __name__ == "__main__":
 some_function()
 print(fibonacci(5))
 print(fibonacci(5))
    
 secret_function()

