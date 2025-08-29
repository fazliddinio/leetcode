import pytest
from .solution import Solution

def test_find_max_average():
    s = Solution()
    assert s.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert s.findMaxAverage([5], 1) == 5.0
