# Singleton Pattern Implementations in Python

This repository demonstrates multiple implementations of the Singleton design pattern in Python. The Singleton pattern
ensures a class has only one instance and provides a global point of access to it.

## Implementations

### 1. Classic Singleton (`singleton.py`)

A traditional implementation using `__new__` and an instance tracking variable.

```python
instance1 = Singleton("First")
instance2 = Singleton("Second")  # Returns the same instance
```

### 2. Decorator-Based Singleton (`decorator_singleton.py`)

A flexible implementation using Python decorators.

```python
@singleton
class DatabaseConnection:


# Class definition...

db1 = DatabaseConnection()
db2 = DatabaseConnection()  # Returns the same instance
```

### 3. Metaclass-Based Singleton (`metaclass_singleton.py`)

An elegant implementation using Python's metaclass feature.

```python
class ConfigManager(metaclass=SingletonMeta):


# Class definition...

config1 = ConfigManager()
config2 = ConfigManager()  # Returns the same instance
```

### 4. Module-Level Singleton (`logger_singleton.py`)

Leverages Python's module behavior as natural singletons.

```python
import logger_singleton as logger

logger.info("This uses the singleton logger instance")
```

### 5. Thread-Safe Singleton (`thread_safe_singleton.py`)

A thread-safe implementation using locks to prevent race conditions.

```python
instance = ThreadSafeSingleton("value")
```

## When to Use the Singleton Pattern

The Singleton pattern is useful when:

- Exactly one instance of a class is needed
- Controlled access to a resource is required
- Global state needs to be managed
- Multiple instances would be problematic (e.g., conflict in resource usage)

## Common Use Cases

- Database connection pools
- Configuration managers
- Logging services
- Device drivers or hardware interfaces
- Caches
- Thread pools

## Design Considerations

1. **Lazy Initialization**: Most implementations here use lazy initialization (create on first use)
2. **Thread Safety**: Consider the `thread_safe_singleton.py` implementation when working with threads
3. **Global State**: Be careful with global state as it can make testing more difficult
4. **Testability**: Singletons can complicate unit testing since they maintain state between tests

## Running the Examples

Each module includes example usage that can be run directly:

```bash
python singleton.py
python decorator_singleton_example.py
# etc.
```

## Learning Points

- Python's `__new__` method and object creation
- Python's decorators and how they can modify class behavior
- Metaclasses in Python
- Module-level variables for simple singletons
- Thread synchronization with locks
