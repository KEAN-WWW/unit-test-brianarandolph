"""Calculator module for basic arithmetic operations."""

def add(a, b):
    """Return the sum of two integers."""
    return a + b

def subtract(a, b):
    """Return the difference of two integers."""
    return a - b

def multiply(a, b):
    """Return the product of two integers."""
    return a * b

def divide(a, b):
    """Return the division of two integers. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


class Calculator:
    """Calculator class with basic arithmetic methods."""

    def add(self, a, b):
        """Return sum of a and b."""
        return add(a, b)

    def subtract(self, a, b):
        """Return difference of a and b."""
        return subtract(a, b)

    def multiply(self, a, b):
        """Return product of a and b."""
        return multiply(a, b)

    def divide(self, a, b):
        """Return division of a by b. Raises ZeroDivisionError if b is 0."""
        return divide(a, b)
