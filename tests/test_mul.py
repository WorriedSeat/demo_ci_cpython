import pytest

from myproject import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (4, 5, 20),
        (0, 10, 0),
        (-2, 3, -6),
        (-2, -8, 16),
    ],
)
def test_mul(a: int, b: int, expected: int) -> None:
    calc = Calculator()
    assert calc.mul(a, b) == expected
