import pytest
from .solution import Solution

def test_largest_rectangle_area():
    s = Solution()
    assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert s.largestRectangleArea([2,4]) == 4
    assert s.largestRectangleArea([2,1,2]) == 3
