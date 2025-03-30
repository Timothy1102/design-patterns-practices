from typing import List

from observer_pattern import Subject, Observer


class WeatherStation(Subject):
    """
    The WeatherStation maintains a state and notifies observers when it changes.
    """
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def attach(self, observer: Observer):
        """
        Attach an observer to the weather station.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Detach an observer from the weather station.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        """
        Notify all observers about weather changes.
        """
        for observer in self._observers:
            observer.update(self)

    def set_measurements(self, temperature, humidity, pressure):
        """
        Set new weather measurements and notify observers.
        """
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

    @property
    def temperature(self):
        """Get the current temperature."""
        return self._temperature

    @property
    def humidity(self):
        """Get the current humidity."""
        return self._humidity

    @property
    def pressure(self):
        """Get the current pressure."""
        return self._pressure
