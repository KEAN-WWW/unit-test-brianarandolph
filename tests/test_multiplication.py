"""Test cases for multiplication in calculator.py"""

from app.calculator import multiply

def test_multiply_positive():
    """Test multiplying two positive numbers"""
    assert multiply(2, 3) == 6

def test_multiply_negative():
    """Test multiplying a negative and positive number"""
    assert multiply(-2, 3) == -6

def test_multiply_zero():
    """Test multiplying by zero"""
    assert multiply(5, 0) == 0
