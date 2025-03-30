def singleton(class_):
    """
    Decorator to convert a class into a singleton.

    This approach allows you to create singletons by simply
    applying the @singleton decorator to any class.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class DatabaseConnection:
    """Example class using the singleton decorator."""

    def __init__(self, connection_string="default_connection"):
        self.connection_string = connection_string
        self.is_connected = False
        print(f"Initializing connection with: {connection_string}")

    def connect(self):
        if not self.is_connected:
            print(f"Connecting to database using {self.connection_string}")
            self.is_connected = True
        else:
            print("Already connected")

    def disconnect(self):
        if self.is_connected:
            print("Disconnecting from database")
            self.is_connected = False
        else:
            print("Already disconnected")


# Example usage
if __name__ == "__main__":
    # First creation
    db1 = DatabaseConnection("production_server")
    db1.connect()

    # Second "creation" - should reuse the same instance
    db2 = DatabaseConnection("test_server")  # This connection string is ignored!

    # Verify they are the same instance
    print(f"Are they the same instance? {db1 is db2}")
    print(f"db1 connection string: {db1.connection_string}")
    print(f"db2 connection string: {db2.connection_string}")  # Will show "production_server"

    # Operations on one instance affect the other
    db2.disconnect()
    print(f"db1 is connected: {db1.is_connected}")  # Will show False
