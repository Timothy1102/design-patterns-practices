# Design Patterns Implementation

A comprehensive collection of software design patterns implemented in Python and TypeScript, with examples, tests, and explanations.

## Overview

This repository serves as a practical reference for common software design patterns, demonstrating their implementation in both Python and TypeScript. Each pattern includes:

- Clean, well-documented implementation
- Unit tests verifying the pattern works as expected
- Real-world examples showing practical applications
- Explanations of when and why to use each pattern

## Patterns Implemented

### Creational Patterns

Patterns that deal with object creation mechanisms:

- **Singleton**: Ensures a class has only one instance and provides a global point of access to it
- **Factory**: Creates objects without specifying the exact class to create

### Structural Patterns

Patterns that focus on object composition or how entities can use each other:

- **Adapter**: Allows incompatible interfaces to work together
- **Decorator**: Dynamically adds responsibilities to objects

### Behavioral Patterns

Patterns that focus on communication between objects:

- **Observer**: Defines a one-to-many dependency between objects so that when one object changes state, all dependents are notified

## Getting Started

### Python Implementation

#### Prerequisites

- Python 3.8+
- pip (Python package installer)

#### Installation

```bash
cd python
pip install -r requirements.txt
```

#### Running Tests

```bash
python -m pytest tests/
```

### TypeScript Implementation

#### Prerequisites

- Node.js 20+
- npm (Node package manager)

#### Installation

```bash
cd typescript
npm install
```

#### Running Tests

```bash
npm test
```

## Project Structure

## Learning Resources

- [O`Reilly - Head First Design Patterns 2nd Edition](https://github.com/ajitpal/BookBank/blob/master/%5BO%60Reilly.%20Head%20First%5D%20-%20Head%20First%20Design%20Patterns%202nd%20Edition%20-%20%5BFreeman%5D.pdf)
- [GoF - Design Patterns Elements of Reusable Object-Oriented Software](https://github.com/GunterMueller/Books-3/blob/master/Design%20Patterns%20Elements%20of%20Reusable%20Object-Oriented%20Software.pdf)
