from abc import ABC, abstractmethod


class Coffee(ABC):
    """
    The Component interface defines operations that can be altered by decorators.
    """
    @abstractmethod
    def get_description(self) -> str:
        """
        Returns a description of the coffee.
        """
        pass

    @abstractmethod
    def cost(self) -> float:
        """
        Returns the cost of the coffee.
        """
        pass


class SimpleCoffee(Coffee):
    """
    Concrete Components provide default implementations of the operations.
    """
    def get_description(self) -> str:
        return "Simple coffee"

    def cost(self) -> float:
        return 2.0
