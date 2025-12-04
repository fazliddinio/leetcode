import pytest
from .solution import Solution, SolutionCopy

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionCopy])
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
    ],
)
def test_move_zeroes(SolutionClass, nums, expected):
    solution = SolutionClass()
    nums_copy = list(nums)
    solution.moveZeroes(nums_copy)
    assert nums_copy == expected