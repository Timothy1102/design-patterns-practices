from abc import ABC, abstractmethod
from python.creational.factory.example1.product import (
    Vehicle,
    Bicycle,
    Car,
    Motorcycle,
    Truck,
)


# --- Factory Method Pattern ---


class VehicleFactory(ABC):
    """
    Creator: The factory interface that declares the factory method.

    The Factory Method pattern uses inheritance to delegate the instantiation
    logic to subclasses.
    """

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        """
        Factory Method: Subclasses will override this to create specific vehicles.

        Returns:
            A new Vehicle instance
        """
        pass

    def deliver_vehicle(self) -> str:
        """
        A template method that uses the factory method.

        This demonstrates how factory methods can be used within template methods.

        Returns:
            A string describing the vehicle delivery process
        """
        # Call the factory method to create a vehicle
        vehicle = self.create_vehicle()

        # Use the vehicle instance
        result = []
        result.append(f"Creating a new {vehicle.get_type()}")
        result.append("Performing quality checks")
        result.append(vehicle.drive())
        result.append("Vehicle is ready for delivery")

        return "\n".join(result)


class CarFactory(VehicleFactory):
    """Concrete Creator: Creates Car objects."""

    def create_vehicle(self) -> Vehicle:
        return Car()


class MotorcycleFactory(VehicleFactory):
    """Concrete Creator: Creates Motorcycle objects."""

    def create_vehicle(self) -> Vehicle:
        return Motorcycle()


class TruckFactory(VehicleFactory):
    """Concrete Creator: Creates Truck objects."""

    def create_vehicle(self) -> Vehicle:
        return Truck()


class BicycleFactory(VehicleFactory):
    """Concrete Creator: Creates Bicycle objects."""

    def create_vehicle(self) -> Vehicle:
        return Bicycle()


def run_factory_method_example():
    """Example demonstrating the Factory Method pattern."""
    print("\n=== Factory Method Example ===")

    # Create factories
    car_factory = CarFactory()
    motorcycle_factory = MotorcycleFactory()
    truck_factory = TruckFactory()
    bicycle_factory = BicycleFactory()

    # Use the template method that calls the factory method
    print("Car Factory:")
    print(car_factory.deliver_vehicle())

    print("\nMotorcycle Factory:")
    print(motorcycle_factory.deliver_vehicle())

    print("\nTruck Factory:")
    print(truck_factory.deliver_vehicle())

    print("\nBicycle Factory:")
    print(bicycle_factory.deliver_vehicle())


if __name__ == "__main__":
    run_factory_method_example()
