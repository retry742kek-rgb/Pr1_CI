def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b

if __name__ == "__main__":
    print(greet("Stas"))
    print("2 + 3 =", add(2, 3))
    print("4 * 5 =", multiply(4, 5))
    print("10 / 2 =", divide(10, 2))
