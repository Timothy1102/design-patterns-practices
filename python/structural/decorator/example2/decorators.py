import functools
import time
from typing import Callable, Any, TypeVar


T = TypeVar('T')


def log_execution(func: Callable[..., T]) -> Callable[..., T]:
    """A decorator that logs when a function starts and finishes execution."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        print(f"LOG: Starting execution of {func.__name__}")
        result = func(*args, **kwargs)
        print(f"LOG: Finished execution of {func.__name__}")
        return result
    return wrapper


def timing_decorator(func: Callable[..., T]) -> Callable[..., T]:
    """A decorator that measures and prints the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"TIMING: {func.__name__} took {(end_time - start_time):.6f} seconds to run")
        return result
    return wrapper


def retry(max_attempts=3, delay_seconds=1):
    """
    A parameterized decorator that retries a function if it raises an exception.

    Args:
        max_attempts: Maximum number of attempts before giving up
        delay_seconds: Seconds to wait between attempts
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"RETRY: Attempt {attempts} failed with error: {e}. Retrying in {delay_seconds} seconds...")
                    time.sleep(delay_seconds)
        return wrapper
    return decorator


def cache_result(func: Callable[..., T]) -> Callable[..., T]:
    """A decorator that caches the results of a function call to avoid repeated computation."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from the function arguments
        # Note: This simple implementation only works for hashable arguments
        key = str(args) + str(kwargs)
        if key not in cache:
            print(f"CACHE: Computing result for {func.__name__}{args}")
            cache[key] = func(*args, **kwargs)
        else:
            print(f"CACHE: Using cached result for {func.__name__}{args}")
        return cache[key]

    return wrapper


def validate_args(validator_func: Callable):
    """
    A decorator that validates function arguments.

    Args:
        validator_func: A function that takes the same arguments as the decorated function
                       and returns True if the arguments are valid, False otherwise.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not validator_func(*args, **kwargs):
                raise ValueError(f"Invalid arguments for {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def deprecated(message: str = "This function is deprecated"):
    """
    Mark a function as deprecated with a custom message.

    Args:
        message: The deprecation message to display
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            print(f"WARNING: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Class decorator example
def singleton(cls):
    """A decorator that ensures a class has only one instance."""
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
