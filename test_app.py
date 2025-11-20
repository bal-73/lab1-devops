from app import add

def test_add():
    assert add(5, 10) == 15

def test_add_negative():
    assert add(-3, -7) == -10

def test_add_zero():
    assert add(0, 0) == 0
