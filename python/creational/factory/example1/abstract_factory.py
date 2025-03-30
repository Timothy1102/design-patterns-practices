from abc import ABC, abstractmethod


# --- Abstract Factory Pattern ---


class LuxuryVehicle(ABC):
    """Abstract Product: Interface for luxury vehicles."""

    @abstractmethod
    def get_features(self) -> str:
        """Return the luxury features."""
        pass


class EconomyVehicle(ABC):
    """Abstract Product: Interface for economy vehicles."""

    @abstractmethod
    def get_efficiency(self) -> str:
        """Return the efficiency rating."""
        pass


class LuxuryCar(LuxuryVehicle):
    """Concrete Product: A luxury car."""

    def get_features(self) -> str:
        return "Leather seats, premium sound system, advanced navigation"


class EconomyCar(EconomyVehicle):
    """Concrete Product: An economy car."""

    def get_efficiency(self) -> str:
        return "35 miles per gallon, low maintenance cost"


class LuxuryMotorcycle(LuxuryVehicle):
    """Concrete Product: A luxury motorcycle."""

    def get_features(self) -> str:
        return "Carbon fiber body, digital dashboard, premium suspension"


class EconomyMotorcycle(EconomyVehicle):
    """Concrete Product: An economy motorcycle."""

    def get_efficiency(self) -> str:
        return "60 miles per gallon, affordable parts"


class VehicleCategoryFactory(ABC):
    """
    Abstract Factory: Interface for creating families of related objects.

    Each concrete factory can produce objects for a specific category or family.
    """

    @abstractmethod
    def create_luxury_vehicle(self) -> LuxuryVehicle:
        """Create a luxury vehicle."""
        pass

    @abstractmethod
    def create_economy_vehicle(self) -> EconomyVehicle:
        """Create an economy vehicle."""
        pass


class CarCategoryFactory(VehicleCategoryFactory):
    """Concrete Factory: Creates different categories of cars."""

    def create_luxury_vehicle(self) -> LuxuryVehicle:
        return LuxuryCar()

    def create_economy_vehicle(self) -> EconomyVehicle:
        return EconomyCar()


class MotorcycleCategoryFactory(VehicleCategoryFactory):
    """Concrete Factory: Creates different categories of motorcycles."""

    def create_luxury_vehicle(self) -> LuxuryVehicle:
        return LuxuryMotorcycle()

    def create_economy_vehicle(self) -> EconomyVehicle:
        return EconomyMotorcycle()


def run_abstract_factory_example():
    """Example demonstrating the Abstract Factory pattern."""
    print("\n=== Abstract Factory Example ===")

    # Create factories for different vehicle categories
    car_category_factory = CarCategoryFactory()
    motorcycle_category_factory = MotorcycleCategoryFactory()

    # Create luxury and economy vehicles using the car factory
    luxury_car = car_category_factory.create_luxury_vehicle()
    economy_car = car_category_factory.create_economy_vehicle()

    # Create luxury and economy vehicles using the motorcycle factory
    luxury_motorcycle = motorcycle_category_factory.create_luxury_vehicle()
    economy_motorcycle = motorcycle_category_factory.create_economy_vehicle()

    # Display the features
    print("Luxury Car Features:", luxury_car.get_features())
    print("Economy Car Efficiency:", economy_car.get_efficiency())
    print("Luxury Motorcycle Features:", luxury_motorcycle.get_features())
    print("Economy Motorcycle Efficiency:", economy_motorcycle.get_efficiency())


if __name__ == "__main__":
    run_abstract_factory_example()
