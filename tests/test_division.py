import pytest
from calculator import divide

def test_division():
    """Test normal division cases."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 1) == 7

def test_divide_zero_exception():
    """Test that dividing by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
