from python.behavioral.decorator.coffee import Coffee


class CoffeeDecorator(Coffee):
    """
    The base Decorator class follows the same interface as the Component.
    The primary purpose is to define the wrapping interface for all concrete decorators.
    """
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    def get_description(self) -> str:
        return self._coffee.get_description()

    def cost(self) -> float:
        return self._coffee.cost()


class MilkDecorator(CoffeeDecorator):
    """
    Concrete Decorators add responsibilities to the component.
    """
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, milk"

    def cost(self) -> float:
        return self.coffee.cost() + 0.5


class WhipDecorator(CoffeeDecorator):
    """
    Concrete Decorators can call parent implementation and then add their own behavior.
    """
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, whip"

    def cost(self) -> float:
        return self.coffee.cost() + 0.7


class VanillaDecorator(CoffeeDecorator):
    """
    Concrete Decorators can execute their behavior before or after the call to a wrapped object.
    """
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, vanilla"

    def cost(self) -> float:
        return self.coffee.cost() + 0.3


class CaramelDecorator(CoffeeDecorator):
    """
    Decorators can execute their behavior in place of the call to the wrapped object.
    """
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, caramel"

    def cost(self) -> float:
        return self.coffee.cost() + 0.6


class SoyDecorator(CoffeeDecorator):
    """
    Decorators can modify return values of the wrapped object.
    """
    def get_description(self) -> str:
        return f"{self.coffee.get_description()}, soy milk"

    def cost(self) -> float:
        return self.coffee.cost() + 0.4


class SizeDecorator(CoffeeDecorator):
    """
    Decorators can also take parameters to modify their behavior.
    """
    def __init__(self, coffee: Coffee, size: str = "medium"):
        super().__init__(coffee)
        self._size = size.lower()
        self._size_factors = {
            "small": 0.8,
            "medium": 1.0,
            "large": 1.3
        }

    def get_description(self) -> str:
        return f"{self._size.capitalize()} {self.coffee.get_description()}"

    def cost(self) -> float:
        factor = self._size_factors.get(self._size, 1.0)
        return self.coffee.cost() * factor


class ExtraShotDecorator(CoffeeDecorator):
    """
    Decorators can define new behavior.
    """
    def __init__(self, coffee: Coffee, shots: int = 1):
        super().__init__(coffee)
        self._shots = shots

    def get_description(self) -> str:
        if self._shots == 1:
            return f"{self.coffee.get_description()}, extra shot"
        return f"{self.coffee.get_description()}, {self._shots} extra shots"

    def cost(self) -> float:
        return self.coffee.cost() + (0.6 * self._shots)
