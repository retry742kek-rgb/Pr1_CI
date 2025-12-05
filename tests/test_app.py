from app import greet, add, multiply

def test_greet():
    assert greet("Bob") == "Hello, Bob!"

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 5) == 10
