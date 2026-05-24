import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_intersect_example1(solution):
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert sorted(solution.intersect(nums1, nums2)) == [2, 2]
    assert sorted(solution.intersect_sorting(nums1.copy(), nums2.copy())) == [2, 2]

def test_intersect_example2(solution):
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert sorted(solution.intersect(nums1, nums2)) == [4, 9]
    assert sorted(solution.intersect_sorting(nums1.copy(), nums2.copy())) == [4, 9]

def test_intersect_empty(solution):
    assert solution.intersect([], [1]) == []
    assert solution.intersect_sorting([], [1]) == []

def test_intersect_no_intersection(solution):
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    assert solution.intersect(nums1, nums2) == []
    assert solution.intersect_sorting(nums1.copy(), nums2.copy()) == []
