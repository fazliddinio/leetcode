import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 1], 1, 3),
        ([1], 0, 0),
    ],
)
def test_subarray_sum(SolutionClass, nums, k, expected):
    solution = SolutionClass()
    assert solution.subarraySum(nums, k) == expected
