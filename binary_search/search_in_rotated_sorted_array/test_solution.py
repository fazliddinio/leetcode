import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([5, 1, 3], 3, 2),
    ],
)
def test_search(SolutionClass, nums, target, expected):
    solution = SolutionClass()
    assert solution.search(nums, target) == expected
