def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Returns the difference between two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Returns the quotient of two numbers. Handles division by zero."""
    if n2 == 0:
        return "Error: Division by zero is undefined."
    return n1 / n2


def exponent(base, power):
    return base ** power
