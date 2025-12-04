import pytest
from .solution import Solution, SolutionBruteForce, SolutionAlternative

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionAlternative])
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1, 5, -2, -4, 0], False),
        ([], False),
        ([1], False),
    ],
)
def test_contains_duplicate(SolutionClass, nums, expected):
    solution = SolutionClass()
    assert solution.containsDuplicate(nums) == expected