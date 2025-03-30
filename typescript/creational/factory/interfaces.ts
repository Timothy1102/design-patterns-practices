// Product interface: defines operations that all concrete products must implement
export interface Vehicle {
    drive(): string;

    getInfo(): VehicleInfo;
}

// Product information structure
export interface VehicleInfo {
    type: string;
    passengerCapacity: number;
    maxSpeed: number;
    fuelType: string;
}
