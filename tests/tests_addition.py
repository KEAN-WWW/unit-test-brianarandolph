from calculator import add

def test_addition():
    """Test addition cases."""
    assert add(2, 3) == 5
    assert add(5, 0) == 5
