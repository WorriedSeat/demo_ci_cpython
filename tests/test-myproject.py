import pytest
from myproject import add, multiply


def test_add_positive():
    assert add(2, 3) == 5
    assert add(0, 0) == 0


def test_add_negative():
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 10) == 0
    assert multiply(-2, 3) == -6


@pytest.mark.parametrize("a,b,expected", [
    (10, 20, 30),
    (-1, -1, -2),
    (0, 5, 5),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected