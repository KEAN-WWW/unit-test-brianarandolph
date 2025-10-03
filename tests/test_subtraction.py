"""Test cases for subtraction in calculator.py"""

from app.calculator import subtract

def test_subtract_positive():
    """Test subtracting smaller from larger number"""
    assert subtract(5, 3) == 2

def test_subtract_negative():
    """Test subtracting negative numbers"""
    assert subtract(-1, -1) == 0

def test_subtract_zero():
    """Test subtracting zero from a number"""
    assert subtract(5, 0) == 5
