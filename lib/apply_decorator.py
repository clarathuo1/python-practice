#A decorator that prints "Decorator Applied" before calling the original function.
def decorator_func(func):
    
    #Returns the decorated function
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper


#Applies the decorator_func decorator to the input function.
def apply_decorator(func):
    
    #Returns the decorated function
    return decorator_func(func)