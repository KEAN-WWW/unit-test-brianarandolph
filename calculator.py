"""Calculator module: functions and Calculator class for basic arithmetic operations."""

def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b

def divide(a: int, b: int) -> float:
    """Return the division of a by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


class Calculator:
    """Calculator class with basic arithmetic methods."""

    def add(self, a: int, b: int) -> int:
        """Return sum of a and b."""
        return add(a, b)

    def subtract(self, a: int, b: int) -> int:
        """Return difference of a and b."""
        return subtract(a, b)

    def multiply(self, a: int, b: int) -> int:
        """Return product of a and b."""
        return multiply(a, b)

    def divide(self, a: int, b: int) -> float:
        """Return division of a by b."""
        return divide(a, b)
