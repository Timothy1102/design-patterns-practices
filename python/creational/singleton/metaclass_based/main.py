class SingletonMeta(type):
    """
    A metaclass that creates a Singleton base class when called.

    This approach uses Python's metaclass feature to control class creation.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Called when you instantiate a class using this metaclass.
        For example: instance = MyClass()
        """
        if cls not in cls._instances:
            # Create a new instance
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigManager(metaclass=SingletonMeta):
    """
    A singleton config manager class.

    Uses the SingletonMeta metaclass to ensure singleton behavior.
    """
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.settings = {}
        print(f"Loading configuration from {config_file}")
        # Simulate loading settings
        self.settings = {"version": "1.0", "environment": "development"}

    def get_setting(self, key):
        """Get a setting value by key."""
        return self.settings.get(key)

    def set_setting(self, key, value):
        """Update a setting value."""
        self.settings[key] = value
        print(f"Updated setting: {key} = {value}")

    def save_settings(self):
        """Simulate saving settings to the config file."""
        print(f"Saving settings to {self.config_file}")


# Example usage
if __name__ == "__main__":
    # Create first instance
    config1 = ConfigManager("app_config.json")
    print(f"Config file: {config1.config_file}")
    print(f"Current settings: {config1.settings}")

    # Create second instance - should return the same instance
    config2 = ConfigManager("backup_config.json")  # This parameter is ignored

    # Verify they are the same
    print(f"Are they the same instance? {config1 is config2}")
    print(f"Config1 file: {config1.config_file}")
    print(f"Config2 file: {config2.config_file}")  # Will show "app_config.json"

    # Modify settings through one instance
    config2.set_setting("environment", "production")

    # Changes reflect in all instances
    print(f"Config1 environment: {config1.get_setting('environment')}")  # Will show "production"
