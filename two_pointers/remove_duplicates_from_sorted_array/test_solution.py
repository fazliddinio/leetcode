import pytest
from .solution import Solution, SolutionPop

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionPop])
@pytest.mark.parametrize(
    "nums, expected_k, expected_nums",
    [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
    ],
)
def test_remove_duplicates(SolutionClass, nums, expected_k, expected_nums):
    solution = SolutionClass()
    nums_copy = list(nums)
    k = solution.removeDuplicates(nums_copy)
    assert k == expected_k
    assert nums_copy[:k] == expected_nums
