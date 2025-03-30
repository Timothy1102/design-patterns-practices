// Observer Pattern Implementation

// Define the interfaces for the Observer pattern
interface Subject {
    registerObserver(observer: Observer): void;

    removeObserver(observer: Observer): void;

    notifyObservers(): void;
}

interface Observer {
    update(data: any): void;
}

// Concrete Subject implementation
class WeatherStation implements Subject {
    private observers: Observer[] = [];
    private temperature: number = 0;
    private humidity: number = 0;
    private pressure: number = 0;

    registerObserver(observer: Observer): void {
        const isExist = this.observers.includes(observer);
        if (!isExist) {
            this.observers.push(observer);
        }
    }

    removeObserver(observer: Observer): void {
        const observerIndex = this.observers.indexOf(observer);
        if (observerIndex !== -1) {
            this.observers.splice(observerIndex, 1);
        }
    }

    notifyObservers(): void {
        for (const observer of this.observers) {
            observer.update({
                temperature: this.temperature,
                humidity: this.humidity,
                pressure: this.pressure
            });
        }
    }

    // Method to simulate measurements changing
    setMeasurements(temperature: number, humidity: number, pressure: number): void {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        this.measurementsChanged();
    }

    private measurementsChanged(): void {
        this.notifyObservers();
    }

    // Additional methods that might be useful but are not part of the pattern
    getTemperature(): number {
        return this.temperature;
    }

    getHumidity(): number {
        return this.humidity;
    }

    getPressure(): number {
        return this.pressure;
    }
}

// Concrete Observer implementations
class CurrentConditionsDisplay implements Observer {
    private temperature: number = 0;
    private humidity: number = 0;

    update(data: any): void {
        this.temperature = data.temperature;
        this.humidity = data.humidity;
        this.display();
    }

    display(): void {
        console.log(`Current conditions: ${this.temperature}°C and ${this.humidity}% humidity`);
    }
}

class StatisticsDisplay implements Observer {
    private temperatureReadings: number[] = [];
    private humidityReadings: number[] = [];
    private pressureReadings: number[] = [];

    update(data: any): void {
        this.temperatureReadings.push(data.temperature);
        this.humidityReadings.push(data.humidity);
        this.pressureReadings.push(data.pressure);
        this.display();
    }

    display(): void {
        const avgTemp = this.calculateAverage(this.temperatureReadings);
        const avgHumidity = this.calculateAverage(this.humidityReadings);
        const avgPressure = this.calculateAverage(this.pressureReadings);

        console.log(`Weather Statistics - Avg temperature: ${avgTemp.toFixed(1)}°C, Avg humidity: ${avgHumidity.toFixed(1)}%, Avg pressure: ${avgPressure.toFixed(1)} hPa`);
    }

    private calculateAverage(readings: number[]): number {
        if (readings.length === 0) return 0;
        const sum = readings.reduce((a, b) => a + b, 0);
        return sum / readings.length;
    }
}

class ForecastDisplay implements Observer {
    private currentPressure: number = 0;
    private lastPressure: number = 0;

    update(data: any): void {
        this.lastPressure = this.currentPressure;
        this.currentPressure = data.pressure;
        this.display();
    }

    display(): void {
        let forecast = "Forecast: ";
        if (this.currentPressure > this.lastPressure) {
            forecast += "Improving weather on the way!";
        } else if (this.currentPressure === this.lastPressure) {
            forecast += "More of the same";
        } else {
            forecast += "Watch out for cooler, rainy weather";
        }
        console.log(forecast);
    }
}

// Example usage
function runExample(): void {
    const weatherStation = new WeatherStation();

    const currentDisplay = new CurrentConditionsDisplay();
    const statisticsDisplay = new StatisticsDisplay();
    const forecastDisplay = new ForecastDisplay();

    // Register observers
    weatherStation.registerObserver(currentDisplay);
    weatherStation.registerObserver(statisticsDisplay);
    weatherStation.registerObserver(forecastDisplay);

    // Simulate weather changes
    console.log("Weather Update 1:");
    weatherStation.setMeasurements(27, 65, 1013);

    console.log("\nWeather Update 2:");
    weatherStation.setMeasurements(28, 70, 1014);

    // Remove an observer
    weatherStation.removeObserver(forecastDisplay);

    console.log("\nWeather Update 3 (without forecast):");
    weatherStation.setMeasurements(26, 75, 1010);
}

// Run the example
runExample();
