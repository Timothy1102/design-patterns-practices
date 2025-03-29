from weather_station import WeatherStation
from weather_observer import WeatherDisplay, AlertSystem, WeatherLogger

def run_weather_example():
    """
    Demonstrates the Observer pattern using a weather station example.
    """
    # Create the subject
    weather_station = WeatherStation()
    
    # Create observers
    phone_display = WeatherDisplay("Phone")
    web_display = WeatherDisplay("Web")
    alert_system = AlertSystem()
    weather_logger = WeatherLogger()
    
    # Register observers with the subject
    weather_station.attach(phone_display)
    weather_station.attach(web_display)
    weather_station.attach(alert_system)
    weather_station.attach(weather_logger)
    
    print("Weather station is operational with all observers attached.")
    
    # Change measurements and trigger notifications
    print("\n--- Setting measurements: 25°C, 65%, 1013 hPa ---")
    weather_station.set_measurements(25, 65, 1013)
    
    # Remove one display
    print("\n--- Detaching Web Display ---")
    weather_station.detach(web_display)
    
    # Change measurements again
    print("\n--- Setting measurements: 32°C, 80%, 1005 hPa ---")
    weather_station.set_measurements(32, 80, 1005)
    
    # Remove alert system
    print("\n--- Detaching Alert System ---")
    weather_station.detach(alert_system)
    
    # Final measurement change
    print("\n--- Setting measurements: -2°C, 30%, 1020 hPa ---")
    weather_station.set_measurements(-2, 30, 1020)


if __name__ == "__main__":
    run_weather_example()
