import {Bus, Car, Truck} from "./classes";
import {Vehicle} from "./interfaces";

// Abstract Factory Pattern: provides an interface for creating families of related or dependent objects

interface TransportationFactory {
    createPassengerVehicle(): Vehicle;

    createCargoVehicle(): Vehicle;
}

class UrbanTransportationFactory implements TransportationFactory {
    createPassengerVehicle(): Vehicle {
        return new Bus();
    }

    createCargoVehicle(): Vehicle {
        return new Truck();
    }
}

class PersonalTransportationFactory implements TransportationFactory {
    createPassengerVehicle(): Vehicle {
        return new Car();
    }

    createCargoVehicle(): Vehicle {
        return new Truck(); // Could use a smaller truck or van here
    }
}

function demonstrateAbstractFactory(): void {
    console.log("\n=== Abstract Factory Demo ===");

    const urbanFactory = new UrbanTransportationFactory();
    const personalFactory = new PersonalTransportationFactory();

    const urbanPassenger = urbanFactory.createPassengerVehicle();
    const urbanCargo = urbanFactory.createCargoVehicle();

    const personalPassenger = personalFactory.createPassengerVehicle();
    const personalCargo = personalFactory.createCargoVehicle();

    console.log(`Urban passenger transport: ${urbanPassenger.getInfo().type} with capacity for ${urbanPassenger.getInfo().passengerCapacity} passengers`);
    console.log(`Urban cargo transport: ${urbanCargo.getInfo().type}`);

    console.log(`Personal passenger transport: ${personalPassenger.getInfo().type} with capacity for ${personalPassenger.getInfo().passengerCapacity} passengers`);
    console.log(`Personal cargo transport: ${personalCargo.getInfo().type}`);
}

demonstrateAbstractFactory();
