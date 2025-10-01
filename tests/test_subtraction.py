from calculator import subtract

def test_subtraction():
    """Test subtraction function."""
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0
    assert subtract(2, 10) == -8
