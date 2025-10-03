"""Test cases for division in calculator.py"""
import pytest
from app.calculator import divide

def test_divide_positive():
    """Test dividing two positive numbers"""
    assert divide(6, 3) == 2

def test_divide_negative():
    """Test dividing a negative number by positive"""
    assert divide(-6, 3) == -2

def test_divide_zero_numerator():
    """Test dividing zero by a positive number"""
    assert divide(0, 5) == 0

def test_divide_zero_denominator():
    """Test dividing by zero raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
