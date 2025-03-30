from python.structural.decorator.example2.decorators import (
    log_execution,
    timing_decorator,
    cache_result,
    deprecated,
    validate_args,
    retry,
    singleton,
)


# Define validator functions
def is_positive_integer(n):
    return isinstance(n, int) and n > 0

def are_positive_integers(*args):
    return all(isinstance(arg, int) and arg > 0 for arg in args)


# Apply multiple decorators
@log_execution
@timing_decorator
@cache_result
def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@deprecated("Use the optimized_factorial function instead")
@validate_args(is_positive_integer)
def factorial(n):
    """Calculate the factorial of n."""
    if n == 1:
        return 1
    return n * factorial(n-1)


@retry(max_attempts=3)
def unreliable_network_call(url):
    """Simulate an unreliable network call that might fail."""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network connection failed")
    return f"Data from {url}"


@singleton
class DatabaseConnection:
    """A singleton database connection class."""
    def __init__(self, connection_string="default"):
        self.connection_string = connection_string
        print(f"Creating new database connection to {connection_string}")

    def query(self, sql):
        return f"Executing query: {sql}"


def run_examples():
    """Run examples demonstrating Python decorators."""
    print("\n--- Fibonacci with caching ---")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(10) again = {fibonacci(10)}")  # Should use cached result

    print("\n--- Factorial with validation ---")
    try:
        print(f"factorial(5) = {factorial(5)}")
        print(f"factorial(-1) = {factorial(-1)}")  # Should raise ValueError
    except ValueError as e:
        print(f"Caught error: {e}")

    print("\n--- Retry decorator ---")
    try:
        result = unreliable_network_call("https://example.com/api")
        print(f"Success: {result}")
    except ConnectionError as e:
        print(f"Failed after retries: {e}")

    print("\n--- Singleton pattern ---")
    conn1 = DatabaseConnection("production")
    conn2 = DatabaseConnection("backup")  # Should not create a new connection
    print(f"Are connections the same object? {conn1 is conn2}")
    print(f"Connection string: {conn1.connection_string}")
    print(f"Connection string: {conn2.connection_string}")


if __name__ == "__main__":
    run_examples()
