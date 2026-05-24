import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findMedianSortedArrays_example1(solution):
    nums1 = [1, 3]
    nums2 = [2]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.0
    assert solution.findMedianSortedArrays_merge(nums1, nums2) == 2.0

def test_findMedianSortedArrays_example2(solution):
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.5
    assert solution.findMedianSortedArrays_merge(nums1, nums2) == 2.5

def test_findMedianSortedArrays_empty(solution):
    nums1 = []
    nums2 = [1]
    assert solution.findMedianSortedArrays(nums1, nums2) == 1.0
    assert solution.findMedianSortedArrays_merge(nums1, nums2) == 1.0
    
def test_findMedianSortedArrays_same_size(solution):
    nums1 = [1, 1]
    nums2 = [1, 2]
    assert solution.findMedianSortedArrays(nums1, nums2) == 1.0
    assert solution.findMedianSortedArrays_merge(nums1, nums2) == 1.0
