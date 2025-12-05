from app import greet, add, multiply, divide

def test_greet():
    assert greet("Bob") == "Hello, Bob!"

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 5) == 10

def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    assert divide(7, 0.5) == 14
