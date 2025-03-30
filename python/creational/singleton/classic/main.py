class Singleton:
    """
    A classic Singleton implementation in Python.

    This implementation ensures that only one instance of the class exists
    and provides a global point of access to it.
    """

    # Private class variable to store the single instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Override the __new__ method to control instance creation.

        Returns:
            The single instance of the class.
        """
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # You might want to add initialization here or in __init__
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, value=None):
        """
        Initialize the singleton instance.
        This will only run once when the instance is first created.

        Args:
            value: Any value to store in the singleton.
        """
        if not self._initialized:
            self.value = value
            self._initialized = True

    def get_value(self):
        """Get the stored value."""
        return self.value

    def set_value(self, value):
        """Set a new value."""
        self.value = value


# Example usage
if __name__ == "__main__":
    # Create first instance
    s1 = Singleton("First value")
    print(f"Instance 1 ID: {id(s1)}")
    print(f"Instance 1 value: {s1.get_value()}")

    # Create second instance - should be the same as the first one
    s2 = Singleton("Second value")  # This value won't actually be set!
    print(f"Instance 2 ID: {id(s2)}")
    print(f"Instance 2 value: {s2.get_value()}")  # Will still show "First value"

    # Verify they are the same instance
    print(f"Are they the same instance? {s1 is s2}")

    # Modify the value through one instance and observe it in the other
    s2.set_value("Value changed")
    print(f"Instance 1 value after change through instance 2: {s1.get_value()}")
