import pytest
from .solution import Solution, SolutionBruteForce, SolutionSorting

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionSorting])
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1, 2, 0, 1], 3),
    ],
)
def test_longest_consecutive(SolutionClass, nums, expected):
    solution = SolutionClass()
    # Copy since sort modifies
    nums_copy = list(nums)
    assert solution.longestConsecutive(nums_copy) == expected
