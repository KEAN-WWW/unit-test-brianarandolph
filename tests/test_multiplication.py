from calculator import multiply

def test_multiplication():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0
    assert multiply(7, 2) == 14
