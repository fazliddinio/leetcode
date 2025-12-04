import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),  # (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
        ([5], 1, 5.0),
        ([0, 4, 0, 3, 2], 1, 4.0),
    ],
)
def test_find_max_average(SolutionClass, nums, k, expected):
    solution = SolutionClass()
    assert solution.findMaxAverage(nums, k) == pytest.approx(expected)
