import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "target, nums, expected",
    [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    ],
)
def test_min_sub_array_len(SolutionClass, target, nums, expected):
    solution = SolutionClass()
    assert solution.minSubArrayLen(target, nums) == expected
