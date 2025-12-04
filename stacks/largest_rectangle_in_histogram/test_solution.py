import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "heights, expected",
    [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1, 1], 2), # Corrected from [1,1] -> 2
    ],
)
def test_largest_rectangle_area(SolutionClass, heights, expected):
    solution = SolutionClass()
    assert solution.largestRectangleArea(heights) == expected
