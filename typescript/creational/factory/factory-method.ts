import {Vehicle} from "./interfaces";
import {Bus, Car, Motorcycle, Truck} from "./classes";

// Factory Method Pattern: defines an interface for creating objects, but lets subclasses decide which classes to instantiate

abstract class VehicleFactory {
    // Factory method
    abstract createVehicle(): Vehicle;

    // Template method that uses the factory method
    deliverVehicle(): string {
        const vehicle = this.createVehicle();
        return `A new ${vehicle.getInfo().type} has been manufactured and is ready for delivery!`;
    }
}

// Concrete Factory implementations
class CarFactory extends VehicleFactory {
    createVehicle(): Vehicle {
        return new Car();
    }
}

class MotorcycleFactory extends VehicleFactory {
    createVehicle(): Vehicle {
        return new Motorcycle();
    }
}

class TruckFactory extends VehicleFactory {
    createVehicle(): Vehicle {
        return new Truck();
    }
}

class BusFactory extends VehicleFactory {
    createVehicle(): Vehicle {
        return new Bus();
    }
}


function demonstrateFactoryMethod(): void {
    console.log("\n=== Factory Method Demo ===");

    const carFactory = new CarFactory();
    const motorcycleFactory = new MotorcycleFactory();
    const truckFactory = new TruckFactory();
    const busFactory = new BusFactory();

    console.log(carFactory.deliverVehicle());
    console.log(motorcycleFactory.deliverVehicle());
    console.log(truckFactory.deliverVehicle());
    console.log(busFactory.deliverVehicle());

    // Using the factory directly
    const motorcycle = motorcycleFactory.createVehicle();
    console.log(`Created a ${motorcycle.getInfo().type} that can go up to ${motorcycle.getInfo().maxSpeed} km/h`);
}

demonstrateFactoryMethod();
