import pytest
from .solution import Solution

def test_min_distance():
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
