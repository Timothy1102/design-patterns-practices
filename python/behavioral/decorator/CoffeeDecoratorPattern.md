# Decorator Design Pattern

## Overview
The Decorator pattern is a structural design pattern that allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class. It is a flexible alternative to subclassing for extending functionality.

## Key Components
1. **Component** (Interface/Abstract Class):
    - Defines the interface for objects that can have responsibilities added to them
    - Example: `Coffee` abstract class

2. **Concrete Component**:
    - The basic object that can be decorated
    - Example: `SimpleCoffee` class

3. **Decorator** (Abstract Class):
    - Maintains a reference to a Component object
    - Conforms to the Component interface
    - Example: `CoffeeDecorator` abstract class

4. **Concrete Decorator**:
    - Adds specific responsibilities to the component
    - Examples: `MilkDecorator`, `WhipDecorator`, `VanillaDecorator`, etc.

## Implementation Details

### Component Interface (`Coffee`)
Defines the common interface for both the original object and the decorated objects:
```python
class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass
        
    @abstractmethod
    def cost(self) -> float:
        pass
```

### Concrete Component (`SimpleCoffee`)
Implements the Component interface:
```python
class SimpleCoffee(Coffee):
    def get_description(self) -> str:
        return "Simple coffee"
        
    def cost(self) -> float:
        return 2.0
```

### Base Decorator (`CoffeeDecorator`)
Maintains a reference to a Component object and implements the Component interface:
```python
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
        
    @property
    def coffee(self) -> Coffee:
        return self._coffee
        
    def get_description(self) -> str:
        return self._coffee.get_description()
        
    def cost(self) -> float:
        return self._coffee.cost()
```

### Concrete Decorators
Examples of concrete decorators that add specific functionality:
```python
class MilkDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, milk"
        
    def cost(self) -> float:
        return self.coffee.cost() + 0.5
```

## Usage Examples

Basic usage:
```python
# Create a simple coffee
coffee = SimpleCoffee()
print(f"{coffee.get_description()} costs ${coffee.cost():.2f}")
# Output: Simple coffee costs $2.00

# Decorate it with milk
milk_coffee = MilkDecorator(coffee)
print(f"{milk_coffee.get_description()} costs ${milk_coffee.cost():.2f}")
# Output: Simple coffee, milk costs $2.50
```

Nested decorators:
```python
# Complex order with multiple decorators
fancy_coffee = VanillaDecorator(WhipDecorator(MilkDecorator(SimpleCoffee())))
print(f"{fancy_coffee.get_description()} costs ${fancy_coffee.cost():.2f}")
# Output: Simple coffee, milk, whip, vanilla costs $3.50
```

Parameterized decorators:
```python
# Using the size decorator
large_coffee = SizeDecorator(SimpleCoffee(), "large")
print(f"{large_coffee.get_description()} costs ${large_coffee.cost():.2f}")
# Output: Large Simple coffee costs $2.60
```

## Benefits of the Decorator Pattern
1. **Open/Closed Principle**: You can extend an object's behavior without modifying its class
2. **Single Responsibility Principle**: You can divide functionality into specific decorator classes
3. **Flexibility**: You can add or remove responsibilities at runtime
4. **Composability**: You can combine multiple decorators to create complex behaviors

## Use Cases
- When you need to add responsibilities to objects dynamically and transparently
- When extension by subclassing is impractical (would lead to a large number of subclasses)
- When you want to add functionality that can be withdrawn
- When you want to stack multiple behaviors in different combinations

## Considerations
- Can result in many small objects that look similar
- Decorators and their components aren't identical, so tests for object type may fail
- Can be harder to understand and debug code with many layers of decoration
