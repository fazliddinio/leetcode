import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_max_area(SolutionClass, height, expected):
    solution = SolutionClass()
    assert solution.maxArea(height) == expected
