import pytest
from .solution import Solution

def test_min_eating_speed():
    s = Solution()
    assert s.minEatingSpeed([3,6,7,11], 8) == 4
    assert s.minEatingSpeed([30,11,23,4,20], 5) == 30
    assert s.minEatingSpeed([30,11,23,4,20], 6) == 23
