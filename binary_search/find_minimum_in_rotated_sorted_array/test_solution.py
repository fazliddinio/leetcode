import pytest
from .solution import Solution

def test_find_min():
    s = Solution()
    assert s.findMin([3,4,5,1,2]) == 1
    assert s.findMin([4,5,6,7,0,1,2]) == 0
    assert s.findMin([11,13,15,17]) == 11
