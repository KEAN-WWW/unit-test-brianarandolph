import pytest
from calculator import divide

def test_divide_positive():
    assert divide(6, 3) == 2

def test_divide_negative():
    assert divide(-6, 3) == -2

def test_divide_zero_numerator():
    assert divide(0, 5) == 0

def test_divide_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
