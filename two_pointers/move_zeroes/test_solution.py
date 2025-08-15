import pytest
from .solution import Solution

def test_move_zeroes():
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    s.moveZeroes(nums)
    assert nums == [0]