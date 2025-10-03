from calculator import subtract

def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-1, -1) == 0

def test_subtract_zero():
    assert subtract(5, 0) == 5
