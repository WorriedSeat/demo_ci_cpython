import pytest

from myproject import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -5, -10),
    ],
)
def test_add(a: int, b: int, expected: int) -> None:
    calc = Calculator()
    assert calc.add(a, b) == expected
