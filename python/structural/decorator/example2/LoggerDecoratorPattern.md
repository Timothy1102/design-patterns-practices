# Decorator Pattern Implementation Using Python Decorators

This implementation shows how Python's built-in decorator syntax can be used
to implement the Decorator design pattern. This approach uses Python's function
decorators rather than the traditional object-oriented implementation with wrapper classes.

## Implemented Decorators

This directory includes several useful decorators that demonstrate different aspects of the pattern:

### Function Decorators

1. **`log_execution`**: Logs when functions are called and their results
2. **`timing_decorator`**: Measures and reports execution time of functions
3. **`cache_result`**: Implements memoization to avoid redundant calculations
4. **`deprecated`**: Marks functions as deprecated with custom warning messages
5. **`validate_args`**: Validates function arguments based on custom predicates
6. **`retry`**: Automatically retries functions that may fail (e.g., network operations)

### Class Decorators

1. **`singleton`**: Ensures that a class has only one instance throughout the application

## Key advantages
- More concise and Pythonic syntax
- Leverages Python's first-class functions
- Easier to apply multiple decorations

## Usage Examples

The main.py file demonstrates how to apply these decorators to various functions:

### Fibonacci with Multiple Decorators

```python
@log_execution
@timing_decorator
@cache_result
def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Input Validation

```python
@deprecated("Use the optimized_factorial function instead")
@validate_args(is_positive_integer)
def factorial(n):
    """Calculate the factorial of n."""
    if n == 1:
        return 1
    return n * factorial(n-1)
```

### Error Handling and Retries

```python
@retry(max_attempts=3)
def unreliable_network_call(url):
    """Simulate an unreliable network call that might fail."""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network connection failed")
    return f"Data from {url}"
```

### Singleton Pattern

```python
@singleton
class DatabaseConnection:
    """A singleton database connection class."""
    def __init__(self, connection_string="default"):
        self.connection_string = connection_string
        print(f"Creating new database connection to {connection_string}")

    def query(self, sql):
        return f"Executing query: {sql}"
```

## Running the Examples

To see all these decorators in action, run the main.py script:

```bash
python main.py
```

This will demonstrate:
- Fibonacci calculation with caching, timing, and logging
- Function validation and deprecation warnings
- Automatic retrying of unreliable operations
- Singleton pattern implementation
