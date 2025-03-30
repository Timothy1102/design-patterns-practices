"""
Decorator Design Pattern Implementation

The Decorator pattern attaches additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending functionality.

Key components:
- Component: Interface for objects that can have responsibilities added to them
- ConcreteComponent: The basic object that can be decorated
- Decorator: Base class for all decorators, maintains a reference to a Component
- ConcreteDecorator: Adds specific responsibilities to the component
"""
from python.structural.decorator.example1.coffee import SimpleCoffee
from python.structural.decorator.example1.decorators import (
    MilkDecorator,
    WhipDecorator,
    VanillaDecorator,
    SizeDecorator,
    CaramelDecorator,
    ExtraShotDecorator,
    SoyDecorator,
)


def run_coffee_example():
    """Example demonstrating the use of the Decorator pattern with a coffee shop scenario."""

    # Create a simple coffee
    coffee = SimpleCoffee()
    print(f"{coffee.get_description()} costs ${coffee.cost():.2f}")

    # Decorate it with milk
    milk_coffee = MilkDecorator(coffee)
    print(f"{milk_coffee.get_description()} costs ${milk_coffee.cost():.2f}")

    # Decorate it with milk and whip
    milk_whip_coffee = WhipDecorator(milk_coffee)
    print(f"{milk_whip_coffee.get_description()} costs ${milk_whip_coffee.cost():.2f}")

    # We can also create decorated coffees directly
    fancy_coffee = VanillaDecorator(WhipDecorator(MilkDecorator(SimpleCoffee())))
    print(f"{fancy_coffee.get_description()} costs ${fancy_coffee.cost():.2f}")

    # Using the size decorator
    large_coffee = SizeDecorator(SimpleCoffee(), "large")
    print(f"{large_coffee.get_description()} costs ${large_coffee.cost():.2f}")

    # Complex order with multiple decorators
    complex_order = SizeDecorator(
        CaramelDecorator(
            ExtraShotDecorator(
                WhipDecorator(
                    SoyDecorator(SimpleCoffee())
                ), 2
            )
        ), "large"
    )
    print(f"{complex_order.get_description()} costs ${complex_order.cost():.2f}")


if __name__ == "__main__":
    run_coffee_example()
