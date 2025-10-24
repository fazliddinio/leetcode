import pytest
from .solution import Solution

def test_find_peak_element():
    s = Solution()
    assert s.findPeakElement([1,2,3,1]) == 2
    # Multiple peaks possible, any valid index is ok for [1,2,1,3,5,6,4]
    # Peak at index 1 (val 2) or index 5 (val 6)
    res = s.findPeakElement([1,2,1,3,5,6,4])
    assert res in [1, 5]
