import pytest
from .solution import Solution, SolutionBruteForce, SolutionSorting

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionSorting])
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([], 0, []),
    ],
)
def test_two_sum(SolutionClass, nums, target, expected):
    solution = SolutionClass()
    result = solution.twoSum(nums, target)
    assert sorted(result) == sorted(expected)
