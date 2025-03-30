# Singleton pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. This is useful when exactly one object is needed to coordinate actions across the system.

## Key aspects of this implementation:

- __new__ method override: This is where the magic happens. The __new__ method controls instance creation before __init__ is called.
- Instance tracking: We use a class variable _instance to store the single instance.
- Initialization flag: The _initialized flag ensures that initialization only happens once, even if the constructor is called multiple times.
- Thread safety: Note that this implementation is not thread-safe. For a thread-safe version, you would need to add locking mechanisms.

## Alternative Implementations:

- Decorator-based Singleton
- Metaclass-based Singleton
- Module-level Singleton (Python modules are singletons by nature)
