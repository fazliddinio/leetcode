import pytest
from .solution import Solution, SolutionSet

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionSet])
@pytest.mark.parametrize(
    "n, expected",
    [
        (19, True),
        (2, False),
    ],
)
def test_is_happy(SolutionClass, n, expected):
    solution = SolutionClass()
    assert solution.isHappy(n) == expected
