from abc import ABC, abstractmethod
from enum import Enum, auto


class VehicleType(Enum):
    """Enum to represent different types of vehicles."""
    CAR = auto()
    MOTORCYCLE = auto()
    TRUCK = auto()
    BICYCLE = auto()


class Vehicle(ABC):
    """Abstract Product: The common interface for all vehicles."""

    @abstractmethod
    def get_type(self) -> str:
        """Return the type of vehicle."""
        pass

    @abstractmethod
    def drive(self) -> str:
        """Simulate driving the vehicle."""
        pass


class Car(Vehicle):
    """Concrete Product: A specific type of vehicle."""

    def get_type(self) -> str:
        return "Car"

    def drive(self) -> str:
        return "Driving a car on the road."

    def park(self) -> str:
        """Car-specific method."""
        return "Parking the car in a parking space."


class Motorcycle(Vehicle):
    """Concrete Product: A specific type of vehicle."""

    def get_type(self) -> str:
        return "Motorcycle"

    def drive(self) -> str:
        return "Riding a motorcycle on the highway."

    def wheelie(self) -> str:
        """Motorcycle-specific method."""
        return "Performing a wheelie!"


class Truck(Vehicle):
    """Concrete Product: A specific type of vehicle."""

    def get_type(self) -> str:
        return "Truck"

    def drive(self) -> str:
        return "Driving a truck to deliver cargo."

    def load_cargo(self, cargo: str) -> str:
        """Truck-specific method."""
        return f"Loading {cargo} into the truck."


class Bicycle(Vehicle):
    """Concrete Product: A specific type of vehicle."""

    def get_type(self) -> str:
        return "Bicycle"

    def drive(self) -> str:
        return "Pedaling a bicycle on the bike path."

    def ring_bell(self) -> str:
        """Bicycle-specific method."""
        return "Ring ring!"
