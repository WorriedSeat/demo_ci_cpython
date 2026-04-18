import pytest

from myproject import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, 5),
        (0, 7, -7),
        (-3, -3, 0),
        (3, -2, 5),
    ],
)
def test_sub(a: int, b: int, expected: int) -> None:
    calc = Calculator()
    assert calc.sub(a, b) == expected
