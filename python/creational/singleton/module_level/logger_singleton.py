"""
Module-level Singleton Implementation

Python modules are singletons by default - they are only loaded once by the
Python interpreter. This makes them a natural way to implement the Singleton pattern.

This file would be saved as 'logger_singleton.py'
"""


class _Logger:
    """
    A private logger class - not meant to be instantiated directly.
    Users should use the pre-created instance through the module's interface.
    """

    def __init__(self):
        self.log_level = "INFO"
        self.logs = []

    def set_level(self, level):
        """Set the logging level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if level.upper() in valid_levels:
            self.log_level = level.upper()
            print(f"Log level set to {self.log_level}")
        else:
            print(f"Invalid log level. Choose from: {', '.join(valid_levels)}")

    def log(self, message, level="INFO"):
        """Log a message at the specified level."""
        if self._should_log(level):
            entry = f"[{level.upper()}] {message}"
            self.logs.append(entry)
            print(entry)

    def _should_log(self, level):
        """Determine if the message should be logged based on current log level."""
        levels = {"DEBUG": 1, "INFO": 2, "WARNING": 3, "ERROR": 4, "CRITICAL": 5}
        return levels.get(level.upper(), 0) >= levels.get(self.log_level, 0)

    def get_logs(self):
        """Return all logged messages."""
        return self.logs


# Create a single instance of the logger
_logger_instance = _Logger()


# Public interface - these are the functions that users of this module should call
def set_level(level):
    """Set the logging level."""
    _logger_instance.set_level(level)


def debug(message):
    """Log a debug message."""
    _logger_instance.log(message, "DEBUG")


def info(message):
    """Log an info message."""
    _logger_instance.log(message, "INFO")


def warning(message):
    """Log a warning message."""
    _logger_instance.log(message, "WARNING")


def error(message):
    """Log an error message."""
    _logger_instance.log(message, "ERROR")


def critical(message):
    """Log a critical message."""
    _logger_instance.log(message, "CRITICAL")


def get_logs():
    """Return all logged messages."""
    return _logger_instance.get_logs()
