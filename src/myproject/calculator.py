class Calculator:
    """Simple arithmetic calculator used for CI demos."""

    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b

    def mul(self, a: int, b: int) -> int:
        return a * b

    def div(self, a: int, b: int) -> float:
        if b == 0:
            raise ZeroDivisionError("division by zero is not allowed")
        return a / b
