import threading

class ThreadSafeSingleton:
    """
    A thread-safe implementation of the Singleton pattern.

    This implementation uses a lock to ensure that only one thread
    can create the instance at a time.
    """
    _instance = None
    _lock = threading.Lock()  # Class level lock for thread safety

    def __new__(cls, *args, **kwargs):
        """
        Thread-safe implementation of singleton instance creation.
        Uses double-checked locking pattern for efficiency.
        """
        # First check (without lock) - for efficiency
        if cls._instance is None:
            # If instance doesn't exist, acquire lock
            with cls._lock:
                # Second check (with lock) - to ensure another thread didn't create the instance
                if cls._instance is None:
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, value=None):
        """Initialize the singleton (runs only once)."""
        if not self._initialized:
            self.value = value
            self._initialized = True


# Example with threads to demonstrate thread safety
import time
import random

def worker(name, value):
    """Worker function that creates a singleton instance."""
    # Add a small random delay to increase chance of race condition
    time.sleep(random.random() * 0.1)

    instance = ThreadSafeSingleton(value)
    print(f"Worker {name} got instance with ID: {id(instance)}, value: {instance.value}")

    # Try to change the value
    time.sleep(random.random() * 0.1)
    old_value = instance.value
    instance.value = f"Changed by {name}"
    print(f"Worker {name} changed value from '{old_value}' to '{instance.value}'")


if __name__ == "__main__":
    # Create multiple threads all trying to create and modify the singleton
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(f"Thread-{i}", f"Value-{i}"))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Verify the final instance
    final = ThreadSafeSingleton()
    print(f"\nFinal instance value: {final.value}")
