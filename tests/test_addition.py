"""Test cases for addition in calculator.py"""

from app.calculator import add

def test_add_positive():
    """Test adding two positive numbers"""
    assert add(2, 3) == 5

def test_add_negative():
    """Test adding two negative numbers"""
    assert add(-1, -1) == -2

def test_add_zero():
    """Test adding zero to a number"""
    assert add(0, 5) == 5
