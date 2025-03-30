from python.creational.factory.example1.product import (
    Vehicle,
    VehicleType,
    Bicycle,
    Car,
    Motorcycle,
    Truck,
)


# --- Simple Factory Pattern ---


class VehicleFactory:
    """
    Simple Factory: Creates different types of vehicles based on input.

    This is not a true Factory Method pattern, but a simple factory
    that's commonly used for its simplicity.
    """

    @staticmethod
    def create_vehicle(vehicle_type: VehicleType) -> Vehicle:
        """
        Create a new vehicle based on the specified type.

        Args:
            vehicle_type: The type of vehicle to create

        Returns:
            A new Vehicle instance

        Raises:
            ValueError: If the vehicle type is not supported
        """
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type == VehicleType.TRUCK:
            return Truck()
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        else:
            raise ValueError(f"Vehicle type {vehicle_type} is not supported")


def run_simple_factory_example():
    """Example demonstrating the Simple Factory pattern."""
    print("\n=== Simple Factory Example ===")

    # Create vehicles using the simple factory
    car = VehicleFactory.create_vehicle(VehicleType.CAR)
    motorcycle = VehicleFactory.create_vehicle(VehicleType.MOTORCYCLE)
    truck = VehicleFactory.create_vehicle(VehicleType.TRUCK)
    bicycle = VehicleFactory.create_vehicle(VehicleType.BICYCLE)

    # Use the vehicles
    print(f"Created a {car.get_type()}: {car.drive()}")
    print(f"Created a {motorcycle.get_type()}: {motorcycle.drive()}")
    print(f"Created a {truck.get_type()}: {truck.drive()}")
    print(f"Created a {bicycle.get_type()}: {bicycle.drive()}")

    # Use type-specific methods
    print(f"Car specific: {car.park()}")
    print(f"Motorcycle specific: {motorcycle.wheelie()}")
    print(f"Truck specific: {truck.load_cargo('furniture')}")
    print(f"Bicycle specific: {bicycle.ring_bell()}")


if __name__ == "__main__":
    run_simple_factory_example()
