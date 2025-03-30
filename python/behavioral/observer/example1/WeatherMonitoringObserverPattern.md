# Observer Pattern Implementation

## Overview
This project demonstrates the Observer Design Pattern in Python. The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Project Structure

- `observer_pattern.py` - Core implementation of the Observer pattern with abstract base classes
- `weather_station.py` - Concrete Subject implementation (WeatherStation)
- `weather_observer.py` - Concrete Observer implementations (WeatherDisplay, AlertSystem, WeatherLogger)
- `main.py` - Example usage demonstrating the pattern in action

## Key Components

### Subject Interface (`observer_pattern.py`)
The Subject maintains a list of observers and provides methods to:
- `attach(observer)`: Register an observer
- `detach(observer)`: Remove an observer
- `notify()`: Notify all registered observers of state changes

### Observer Interface (`observer_pattern.py`)
The Observer interface declares the update method that subjects use to notify observers:
- `update(subject)`: Called when the subject's state changes

### Concrete Subject - WeatherStation (`weather_station.py`)
A weather monitoring station that:
- Maintains weather measurements (temperature, humidity, pressure)
- Implements the Subject interface
- Notifies observers when measurements change

### Concrete Observers (`weather_observer.py`)
Several observer implementations that react to weather changes:
1. **WeatherDisplay**: Shows weather data on different platforms
2. **AlertSystem**: Generates alerts based on weather conditions
3. **WeatherLogger**: Logs all weather changes

## How the Observer Pattern Works in This Implementation

1. The `WeatherStation` (Subject) maintains a list of observers.
2. Observers register with the `WeatherStation` using the `attach()` method.
3. When the weather measurements change via `set_measurements()`, the `WeatherStation` calls `notify()`.
4. The `notify()` method iterates through all registered observers and calls their `update()` method.
5. Each observer receives the current state and responds according to its specific implementation.

## Example Usage

```python
# Create the subject
weather_station = WeatherStation()

# Create observers
phone_display = WeatherDisplay("Phone")
alert_system = AlertSystem()

# Register observers
weather_station.attach(phone_display)
weather_station.attach(alert_system)

# Change state, which triggers notifications
weather_station.set_measurements(25, 65, 1013)

# Remove an observer
weather_station.detach(alert_system)
```

## Benefits of the Observer Pattern

- **Loose coupling**: Subjects and observers are decoupled, allowing them to vary independently
- **Dynamic relationships**: Observers can be added or removed at runtime
- **Support for broadcast communication**: One change triggers updates to multiple objects
- **Open/Closed Principle**: New observers can be added without modifying the subject

## Use Cases

This pattern is particularly useful for:
- Event handling systems
- Model-View-Controller architectures
- Real-time data monitoring
- Publish-subscribe systems
