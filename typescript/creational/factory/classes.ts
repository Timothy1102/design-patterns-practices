import {Vehicle, VehicleInfo} from "./interfaces";

// Concrete Product implementations

export class Car implements Vehicle {
    private info: VehicleInfo = {
        type: 'Car',
        passengerCapacity: 5,
        maxSpeed: 180,
        fuelType: 'Gasoline'
    };

    drive(): string {
        return 'Driving a car on the road.';
    }

    getInfo(): VehicleInfo {
        return this.info;
    }
}

export class Motorcycle implements Vehicle {
    private info: VehicleInfo = {
        type: 'Motorcycle',
        passengerCapacity: 2,
        maxSpeed: 220,
        fuelType: 'Gasoline'
    };

    drive(): string {
        return 'Riding a motorcycle at high speed.';
    }

    getInfo(): VehicleInfo {
        return this.info;
    }
}

export class Truck implements Vehicle {
    private info: VehicleInfo = {
        type: 'Truck',
        passengerCapacity: 3,
        maxSpeed: 140,
        fuelType: 'Diesel'
    };

    drive(): string {
        return 'Operating a truck to transport cargo.';
    }

    getInfo(): VehicleInfo {
        return this.info;
    }
}

export class Bus implements Vehicle {
    private info: VehicleInfo = {
        type: 'Bus',
        passengerCapacity: 50,
        maxSpeed: 120,
        fuelType: 'Diesel'
    };

    drive(): string {
        return 'Driving a bus with many passengers.';
    }

    getInfo(): VehicleInfo {
        return this.info;
    }
}
