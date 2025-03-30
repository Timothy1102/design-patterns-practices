# Factory Pattern Implementation in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Types of Factory Patterns](#types-of-factory-patterns)
    - [Simple Factory](#simple-factory)
    - [Factory Method](#factory-method)
    - [Abstract Factory](#abstract-factory)
3. [Implementation Examples](#implementation-examples)
    - [Vehicle Factory Implementation](#vehicle-factory-implementation)
4. [Use Cases](#use-cases)
5. [Benefits and Drawbacks](#benefits-and-drawbacks)
6. [Best Practices](#best-practices)
7. [Code Examples](#code-examples)
8. [References](#references)

## Introduction

The Factory pattern is a creational design pattern that provides an interface for creating objects without specifying
their concrete classes. It encapsulates the object creation logic, making code more maintainable and less coupled to
specific implementations.

The core idea behind the Factory pattern is to create objects through a factory rather than direct instantiation using
the `new` keyword (or in Python's case, calling the class directly). This provides several advantages, including
encapsulation, abstraction, and simplified maintenance.

## Types of Factory Patterns

There are three main variations of the Factory pattern:

### Simple Factory

The Simple Factory (sometimes called Static Factory) is the most basic form of a factory. It's not technically one of
the original Gang of Four design patterns but is widely used due to its simplicity.

**Key characteristics:**

- A single factory class with a method that creates objects based on input parameters
- Centralizes object creation logic
- Typically uses a switch statement or if-else logic to determine which object to create

```python
class SimpleFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "A":
            return ProductA()
        elif product_type == "B":
            return ProductB()
```

### Factory Method

The Factory Method pattern defines an interface for creating objects but lets subclasses decide which classes to
instantiate. It enables a class to defer instantiation to subclasses.

**Key characteristics:**

- An abstract Creator class with a factory method
- Concrete Creator subclasses that override the factory method
- Uses inheritance to vary the object creation
- Often used within template methods

```python
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
        
    def some_operation(self):
        # Call the factory method to create a Product object
        product = self.factory_method()
        # Use the product
        return product.operation()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()
```

### Abstract Factory

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without
specifying their concrete classes.

**Key characteristics:**

- Defines interfaces for multiple factories, each capable of creating different product objects
- Enforces consistency among products
- Useful when a system needs to be independent of how its products are created
- Supports the creation of products that work together

```python
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass
        
    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()
        
    def create_product_b(self):
        return ProductB1()
```

## Implementation Examples

### Vehicle Factory Implementation

Our implementation uses the vehicle domain to demonstrate all three factory patterns. Here's an overview:

#### Simple Factory for Vehicles

This implementation creates different types of vehicles (Car, Motorcycle, Truck, Bicycle) based on a vehicle type
parameter.

```python
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType) -> Vehicle:
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        # ...and so on
```

#### Factory Method for Vehicle Production

This implementation uses different factory classes (CarFactory, MotorcycleFactory, etc.) that inherit from a common
VehicleFactory interface to create specific types of vehicles.

```python
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass
    
    def deliver_vehicle(self) -> str:
        vehicle = self.create_vehicle()
        # Use the vehicle in a template method
        # ...

class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()
```

#### Abstract Factory for Vehicle Categories

This implementation creates families of related vehicles - luxury and economy versions of different vehicle types.

```python
class VehicleCategoryFactory(ABC):
    @abstractmethod
    def create_luxury_vehicle(self) -> LuxuryVehicle:
        pass
    
    @abstractmethod
    def create_economy_vehicle(self) -> EconomyVehicle:
        pass

class CarCategoryFactory(VehicleCategoryFactory):
    def create_luxury_vehicle(self) -> LuxuryVehicle:
        return LuxuryCar()
    
    def create_economy_vehicle(self) -> EconomyVehicle:
        return EconomyCar()
```

## Use Cases

The Factory pattern is particularly useful in the following scenarios:

1. **When a class can't anticipate the type of objects it must create**
    - For example, a framework that needs to create different UI elements based on user configurations

2. **When a class wants its subclasses to specify the objects it creates**
    - This allows for extension of the system with new types of products without modifying existing code

3. **When you want to encapsulate the creation of complex objects**
    - Hiding the details of object construction and making the client code more focused on usage rather than creation

4. **When you need to control the lifecycle of objects**
    - Factories can be used to implement object pooling or caching strategies

5. **When you need to work with families of related objects**
    - The Abstract Factory pattern is particularly useful for creating coherent sets of objects

## Benefits and Drawbacks

### Benefits

1. **Loose coupling**: Clients depend on interfaces rather than concrete classes
2. **Single Responsibility Principle**: Moves object creation logic to a single place
3. **Open/Closed Principle**: System can be extended with new products without modifying existing code
4. **Encapsulation**: Hides the complexity of object creation
5. **Consistency**: Ensures objects are created in a consistent manner

### Drawbacks

1. **Complexity**: Introduces additional classes, which can increase complexity
2. **Over-engineering**: For simple cases, direct instantiation might be clearer
3. **Inheritance limitations**: The Factory Method pattern relies on inheritance, which can be inflexible
4. **Runtime performance**: Additional method calls can impact performance in critical sections

## Best Practices

1. **Use clear naming conventions**:
    - Factory classes should have names like `ProductFactory` or `ProductCreator`
    - Factory methods should have names like `createProduct()` or `makeProduct()`

2. **Return the most abstract type possible**:
    - Factories should return interfaces or abstract classes, not concrete classes

3. **Consider parameterized factories**:
    - Allow factories to be configured or parameterized for more flexibility

4. **Validate inputs**:
    - Factory methods should validate their parameters and throw appropriate exceptions

5. **Use singletons for factories when appropriate**:
    - Many factories don't need state, so they can be implemented as singletons or with static methods

## Code Examples

### Simple Factory Example

```python
# Create vehicles using the simple factory
car = VehicleFactory.create_vehicle(VehicleType.CAR)
motorcycle = VehicleFactory.create_vehicle(VehicleType.MOTORCYCLE)

# Use the vehicles
print(f"Created a {car.get_type()}: {car.drive()}")
print(f"Created a {motorcycle.get_type()}: {motorcycle.drive()}")
```

### Factory Method Example

```python
# Create factories
car_factory = CarFactory()
motorcycle_factory = MotorcycleFactory()

# Use the template method that calls the factory method
print("Car Factory:")
print(car_factory.deliver_vehicle())

print("\nMotorcycle Factory:")
print(motorcycle_factory.deliver_vehicle())
```

### Abstract Factory Example

```python
# Create factories for different vehicle categories
car_category_factory = CarCategoryFactory()
motorcycle_category_factory = MotorcycleCategoryFactory()

# Create luxury and economy vehicles using the car factory
luxury_car = car_category_factory.create_luxury_vehicle()
economy_car = car_category_factory.create_economy_vehicle()

# Display the features
print("Luxury Car Features:", luxury_car.get_features())
print("Economy Car Efficiency:", economy_car.get_efficiency())
```

## References

1. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). Design Patterns: Elements of Reusable Object-Oriented
   Software. Addison-Wesley.
2. Freeman, E., Robson, E., Bates, B., & Sierra, K. (2004). Head First Design Patterns. O'Reilly Media.
