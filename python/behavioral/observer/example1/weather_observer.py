from observer_pattern import Observer

class WeatherDisplay(Observer):
    """
    Display that shows current weather conditions.
    """
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        """
        Display weather updates from the weather station.
        """
        print(f"\n{self.name} Display:")
        print(f"Temperature: {subject.temperature}°C")
        print(f"Humidity: {subject.humidity}%")
        print(f"Pressure: {subject.pressure} hPa")

class AlertSystem(Observer):
    """
    Alert system that notifies when weather conditions reach critical values.
    """
    def update(self, subject):
        """
        Check weather conditions and issue alerts if necessary.
        """
        warnings = []

        # Temperature alerts
        if subject.temperature > 30:
            warnings.append("HEAT WARNING: Temperature above 30°C")
        elif subject.temperature < 0:
            warnings.append("FROST WARNING: Temperature below 0°C")

        # Humidity alerts
        if subject.humidity > 90:
            warnings.append("HIGH HUMIDITY WARNING: Humidity above 90%")
        elif subject.humidity < 20:
            warnings.append("LOW HUMIDITY WARNING: Very dry conditions")

        # Pressure alerts
        if subject.pressure < 970:
            warnings.append("STORM WARNING: Low pressure system")
        elif subject.pressure > 1040:
            warnings.append("HIGH PRESSURE: Stable weather system")

        if warnings:
            print("\nWEATHER ALERTS:")
            for warning in warnings:
                print(f" - {warning}")

class WeatherLogger(Observer):
    """
    Logger that records weather data for analysis.
    """
    def update(self, subject):
        """
        Log weather data from the weather station.
        """
        log_entry = (
            f"TIME: {self._get_current_time()}, "
            f"TEMP: {subject.temperature}°C, "
            f"HUMIDITY: {subject.humidity}%, "
            f"PRESSURE: {subject.pressure} hPa"
        )
        
        print("\nWeather Log Entry:")
        print(log_entry)
        print("Data logged to weather.log")
        
        # In a real implementation, we would actually write to a file here
        # with open('weather.log', 'a') as log_file:
        #     log_file.write(log_entry + '\n')

    def _get_current_time(self):
        """Get current time for logging purposes."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
