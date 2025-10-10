import pytest
from .solution import Solution

def test_next_greater_element():
    s = Solution()
    assert s.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert s.nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]
