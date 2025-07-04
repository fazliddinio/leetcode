import pytest
from .solution import Solution

def test_merge():
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    s.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    s.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    s.merge(nums1, 0, [1], 1)
    assert nums1 == [1]