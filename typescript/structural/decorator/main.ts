// Decorator Pattern Implementation

// Component Interface - defines operations that can be altered by decorators
interface Coffee {
    getDescription(): string;
    getCost(): number;
}

// Concrete Component - implements the base component interface
class SimpleCoffee implements Coffee {
    getDescription(): string {
        return "Simple Coffee";
    }

    getCost(): number {
        return 5;
    }
}

// Base Decorator - maintains a reference to a Component object and implements the same interface
abstract class CoffeeDecorator implements Coffee {
    protected decoratedCoffee: Coffee;

    constructor(coffee: Coffee) {
        this.decoratedCoffee = coffee;
    }

    getDescription(): string {
        return this.decoratedCoffee.getDescription();
    }

    getCost(): number {
        return this.decoratedCoffee.getCost();
    }
}

// Concrete Decorators - add responsibilities to components

class MilkDecorator extends CoffeeDecorator {
    constructor(coffee: Coffee) {
        super(coffee);
    }

    getDescription(): string {
        return `${this.decoratedCoffee.getDescription()}, Milk`;
    }

    getCost(): number {
        return this.decoratedCoffee.getCost() + 1.5;
    }
}

class WhippedCreamDecorator extends CoffeeDecorator {
    constructor(coffee: Coffee) {
        super(coffee);
    }

    getDescription(): string {
        return `${this.decoratedCoffee.getDescription()}, Whipped Cream`;
    }

    getCost(): number {
        return this.decoratedCoffee.getCost() + 2.0;
    }
}

class CaramelDecorator extends CoffeeDecorator {
    constructor(coffee: Coffee) {
        super(coffee);
    }

    getDescription(): string {
        return `${this.decoratedCoffee.getDescription()}, Caramel`;
    }

    getCost(): number {
        return this.decoratedCoffee.getCost() + 2.5;
    }
}

class VanillaDecorator extends CoffeeDecorator {
    constructor(coffee: Coffee) {
        super(coffee);
    }

    getDescription(): string {
        return `${this.decoratedCoffee.getDescription()}, Vanilla`;
    }

    getCost(): number {
        return this.decoratedCoffee.getCost() + 1.8;
    }
}

class ChocolateDecorator extends CoffeeDecorator {
    constructor(coffee: Coffee) {
        super(coffee);
    }

    getDescription(): string {
        return `${this.decoratedCoffee.getDescription()}, Chocolate`;
    }

    getCost(): number {
        return this.decoratedCoffee.getCost() + 2.2;
    }
}

class EspressoShotDecorator extends CoffeeDecorator {
    constructor(coffee: Coffee) {
        super(coffee);
    }

    getDescription(): string {
        return `${this.decoratedCoffee.getDescription()}, Extra Espresso Shot`;
    }

    getCost(): number {
        return this.decoratedCoffee.getCost() + 3.0;
    }
}

// More complex component types
class DarkRoast implements Coffee {
    getDescription(): string {
        return "Dark Roast Coffee";
    }

    getCost(): number {
        return 6;
    }
}

class Decaf implements Coffee {
    getDescription(): string {
        return "Decaf Coffee";
    }

    getCost(): number {
        return 5.5;
    }
}

class Espresso implements Coffee {
    getDescription(): string {
        return "Espresso";
    }

    getCost(): number {
        return 6.5;
    }
}

// Size decorator - an alternative approach using composition
interface CoffeeSize {
    getDescription(): string;
    getCostMultiplier(): number;
}

class SizeDecorator extends CoffeeDecorator {
    private size: CoffeeSize;

    constructor(coffee: Coffee, size: CoffeeSize) {
        super(coffee);
        this.size = size;
    }

    getDescription(): string {
        return `${this.size.getDescription()} ${this.decoratedCoffee.getDescription()}`;
    }

    getCost(): number {
        return this.decoratedCoffee.getCost() * this.size.getCostMultiplier();
    }
}

class SmallSize implements CoffeeSize {
    getDescription(): string {
        return "Small";
    }

    getCostMultiplier(): number {
        return 0.8;
    }
}

class MediumSize implements CoffeeSize {
    getDescription(): string {
        return "Medium";
    }

    getCostMultiplier(): number {
        return 1.0;
    }
}

class LargeSize implements CoffeeSize {
    getDescription(): string {
        return "Large";
    }

    getCostMultiplier(): number {
        return 1.2;
    }
}

// Example of a Printable decorator that adds a new method (structural extension)
interface Printable {
    print(): void;
}

class PrintableDecorator extends CoffeeDecorator implements Printable {
    constructor(coffee: Coffee) {
        super(coffee);
    }

    // Implements the method from the Printable interface
    print(): void {
        console.log(`Printing receipt for: ${this.getDescription()}, Cost: $${this.getCost().toFixed(2)}`);
    }
}

// Demo function to show how the pattern works
function demonstrateDecoratorPattern(): void {
    console.log("=== Coffee Shop Menu System Using Decorator Pattern ===\n");

    // Create a simple coffee
    console.log("Ordering a simple coffee:");
    let coffee: Coffee = new SimpleCoffee();
    console.log(`Description: ${coffee.getDescription()}`);
    console.log(`Cost: $${coffee.getCost().toFixed(2)}\n`);

    // Add milk to the coffee
    console.log("Adding milk to the coffee:");
    coffee = new MilkDecorator(coffee);
    console.log(`Description: ${coffee.getDescription()}`);
    console.log(`Cost: $${coffee.getCost().toFixed(2)}\n`);

    // Add whipped cream to the coffee with milk
    console.log("Adding whipped cream to the coffee with milk:");
    coffee = new WhippedCreamDecorator(coffee);
    console.log(`Description: ${coffee.getDescription()}`);
    console.log(`Cost: $${coffee.getCost().toFixed(2)}\n`);

    // Create an espresso with multiple decorators at once
    console.log("Creating a vanilla caramel espresso with whipped cream:");
    let specialCoffee: Coffee = new Espresso();
    specialCoffee = new VanillaDecorator(specialCoffee);
    specialCoffee = new CaramelDecorator(specialCoffee);
    specialCoffee = new WhippedCreamDecorator(specialCoffee);
    console.log(`Description: ${specialCoffee.getDescription()}`);
    console.log(`Cost: $${specialCoffee.getCost().toFixed(2)}\n`);

    // Using size decorators
    console.log("Ordering coffees of different sizes:");
    const smallCoffee = new SizeDecorator(new DarkRoast(), new SmallSize());
    console.log(`Description: ${smallCoffee.getDescription()}`);
    console.log(`Cost: $${smallCoffee.getCost().toFixed(2)}`);

    const mediumCoffee = new SizeDecorator(new DarkRoast(), new MediumSize());
    console.log(`Description: ${mediumCoffee.getDescription()}`);
    console.log(`Cost: $${mediumCoffee.getCost().toFixed(2)}`);

    const largeCoffee = new SizeDecorator(new DarkRoast(), new LargeSize());
    console.log(`Description: ${largeCoffee.getDescription()}`);
    console.log(`Cost: $${largeCoffee.getCost().toFixed(2)}\n`);

    // Creating a complex drink using chained decorations
    console.log("Creating a large decaf with milk, chocolate, and an extra shot:");
    let complexDrink: Coffee = new Decaf();
    complexDrink = new MilkDecorator(complexDrink);
    complexDrink = new ChocolateDecorator(complexDrink);
    complexDrink = new EspressoShotDecorator(complexDrink);
    complexDrink = new SizeDecorator(complexDrink, new LargeSize());
    console.log(`Description: ${complexDrink.getDescription()}`);
    console.log(`Cost: $${complexDrink.getCost().toFixed(2)}\n`);

    // Example of a structural decorator that adds new methods
    console.log("Using a structural decorator to add a print method:");
    const printableCoffee = new PrintableDecorator(
        new WhippedCreamDecorator(
            new MilkDecorator(
                new SimpleCoffee()
            )
        )
    );
    printableCoffee.print();
}

// Run the demonstration
demonstrateDecoratorPattern();
