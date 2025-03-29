"""
Observer Design Pattern Implementation

The Observer pattern defines a one-to-many dependency between objects so that
when one object changes state, all its dependents are notified and updated automatically.

Key components:
- Subject: Maintains a list of observers and notifies them of state changes
- Observer: Interface that defines the update method for observers
- ConcreteObserver: Implements the Observer interface to respond to updates
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects
    to notify observers about changes in their state.
    """
    @abstractmethod
    def update(self, subject):
        """
        Receive update from subject.
        """
        pass

class Subject(ABC):
    """
    The Subject interface declares methods for managing observers.
    """
    @abstractmethod
    def attach(self, observer):
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer):
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """
        pass
