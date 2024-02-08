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

# Example usage:
# updated file
@timer
def some_function():
    time.sleep(2)
    print("Function executed")

if __name__ == "__main__":
 some_function()
