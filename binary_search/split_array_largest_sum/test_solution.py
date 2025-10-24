import pytest
from .solution import Solution

def test_split_array():
    s = Solution()
    assert s.splitArray([7,2,5,10,8], 2) == 18
    assert s.splitArray([1,2,3,4,5], 2) == 9
