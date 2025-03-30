import {Vehicle} from "./interfaces";
import {Bus, Car, Motorcycle, Truck} from "./classes";

// Simple Factory (not technically the Factory Pattern, but often used and confused with it)

class SimpleVehicleFactory {
    createVehicle(type: string): Vehicle {
        switch (type.toLowerCase()) {
            case 'car':
                return new Car();
            case 'motorcycle':
                return new Motorcycle();
            case 'truck':
                return new Truck();
            case 'bus':
                return new Bus();
            default:
                throw new Error(`Vehicle type "${type}" is not supported.`);
        }
    }
}

function demonstrateSimpleFactory(): void {
    console.log("=== Simple Factory Demo ===");
    const factory = new SimpleVehicleFactory();

    try {
        const car = factory.createVehicle('car');
        const motorcycle = factory.createVehicle('motorcycle');
        const truck = factory.createVehicle('truck');

        console.log(car.drive());
        console.log(`Car info: ${JSON.stringify(car.getInfo())}`);

        console.log(motorcycle.drive());
        console.log(`Motorcycle info: ${JSON.stringify(motorcycle.getInfo())}`);

        console.log(truck.drive());
        console.log(`Truck info: ${JSON.stringify(truck.getInfo())}`);

        // This will throw an error
        // const invalid = factory.createVehicle('submarine');
    } catch (error) {
        console.error('Error:', error.message);
    }
}

demonstrateSimpleFactory();
