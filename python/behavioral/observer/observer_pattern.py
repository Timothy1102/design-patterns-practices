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
