import pytest
from .solution import Solution

def test_climb_stairs():
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
