import pytest
from .solution import Solution, SolutionBruteForce, SolutionHash

def sort_result(result):
    """Sorts result for comparison."""
    # Sort each triplet, then sort the list of triplets
    return sorted([sorted(triplet) for triplet in result])

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionHash])
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
    ],
)
def test_three_sum(SolutionClass, nums, expected):
    solution = SolutionClass()
    # Copy input as sort modifies it
    nums_copy = list(nums)
    result = solution.threeSum(nums_copy)
    assert sort_result(result) == sort_result(expected)
