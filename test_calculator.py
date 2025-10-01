"""Tests for calculator.py module."""
import pytest
from calculator import add, subtract, multiply, divide, Calculator

def test_add():
    """Test add function."""
    assert add(2, 3) == 5

def test_subtract():
    """Test subtract function."""
    assert subtract(5, 2) == 3

def test_multiply():
    """Test multiply function."""
    assert multiply(3, 4) == 12

def test_divide():
    """Test divide function."""
    assert divide(10, 2) == 5

def test_divide_zero():
    """Test divide function raises ZeroDivisionError on division by zero."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_class_add():
    """Test Calculator.add method."""
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_class_subtract():
    """Test Calculator.subtract method."""
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_class_multiply():
    """Test Calculator.multiply method."""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_class_divide():
    """Test Calculator.divide method."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_class_divide_zero():
    """Test Calculator.divide method raises ZeroDivisionError."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
