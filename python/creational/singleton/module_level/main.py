"""
Usage example for the module-level singleton logger.
This would be saved as a separate file from the logger implementation.
"""

# Import the logger module
import logger_singleton as logger


# Example usage in one part of the application
def main_process():
    logger.info("Starting main process")
    logger.debug("This debug message won't appear with default INFO level")

    # Change log level
    logger.set_level("DEBUG")
    logger.debug("Now this debug message will appear")

    # Log an error
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.error("Division by zero error")


# Example usage in another part of the application
def another_process():
    logger.warning("This is a warning from another process")
    # The log level is still DEBUG because we're using the same singleton instance
    logger.debug("This debug message will appear because log level is DEBUG")


if __name__ == "__main__":
    print("=== Running main process ===")
    main_process()

    print("\n=== Running another process ===")
    another_process()

    print("\n=== All logs ===")
    for log in logger.get_logs():
        print(log)
