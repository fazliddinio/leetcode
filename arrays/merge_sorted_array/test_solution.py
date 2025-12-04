import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_merge(SolutionClass, nums1, m, nums2, n, expected):
    solution = SolutionClass()
    # We need a fresh copy of nums1 because the solution modifies it in-place
    # The parametrization gives us a reference, so for each solution class/test case we must be careful.
    # Actually pytest parametrization passes the same object if mutable lists are defined in the decorator.
    # Better to copy inside the test function if we were modifying the same list, but here
    # 'nums1' is created fresh for each test case invocation IF it was a fixture or if pytest recreates it.
    # But list literals in parametrization are shared across tests? Let's check.
    # Pytest parametrise arguments are evaluated once. So we should copy nums1.
    
    nums1_copy = list(nums1) 
    solution.merge(nums1_copy, m, nums2, n)
    assert nums1_copy == expected