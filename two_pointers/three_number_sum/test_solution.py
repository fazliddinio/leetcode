import pytest
from .solution import Solution

def test_three_number_sum():
    s = Solution()
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    res = s.threeNumberSum(arr, target)
    # Solution sorts the triplets
    assert res == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
