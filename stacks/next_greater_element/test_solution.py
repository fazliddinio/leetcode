import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
    ],
)
def test_next_greater_element(SolutionClass, nums1, nums2, expected):
    solution = SolutionClass()
    assert solution.nextGreaterElement(nums1, nums2) == expected
