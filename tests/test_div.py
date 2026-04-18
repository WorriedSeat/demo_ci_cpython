import pytest

from src.myproject import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (8, 2, 4.0),
        (7, 2, 3.5),
        (-9, 3, -3.0),
    ],
)
def test_div(a: int, b: int, expected: float) -> None:
    calc = Calculator()
    assert calc.div(a, b) == expected


def test_div_by_zero_raises() -> None:
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(10, 0)
