import pytest
from .solution import Solution

def test_find_median_sorted_arrays():
    s = Solution()
    assert s.findMedianSortedArrays([1,3], [2]) == 2.00000
    assert s.findMedianSortedArrays([1,2], [3,4]) == 2.50000
