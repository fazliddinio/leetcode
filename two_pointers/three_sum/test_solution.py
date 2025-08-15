import pytest
from .solution import Solution

def test_three_sum():
    s = Solution()
    # Order of triplets or elements inside doesn't matter for correctness but test needs to handle it.
    # The solution sorts internal elements, so we sort triplets.
    res = s.threeSum([-1, 0, 1, 2, -1, -4])
    res = sorted([sorted(x) for x in res])
    assert res == [[-1, -1, 2], [-1, 0, 1]]

    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
