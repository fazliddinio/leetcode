import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_merge_example1(solution):
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1_b = [1, 2, 3, 0, 0, 0]
    solution.merge_sorting(nums1_b, 3, nums2, 3)
    assert nums1_b == [1, 2, 2, 3, 5, 6]

def test_merge_example2(solution):
    nums1 = [1]
    nums2 = []
    solution.merge(nums1, 1, nums2, 0)
    assert nums1 == [1]

    nums1_b = [1]
    solution.merge_sorting(nums1_b, 1, nums2, 0)
    assert nums1_b == [1]

def test_merge_example3(solution):
    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, 1)
    assert nums1 == [1]

    nums1_b = [0]
    solution.merge_sorting(nums1_b, 0, nums2, 1)
    assert nums1_b == [1]
