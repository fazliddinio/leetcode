import pytest
from .solution import Solution

def test_remove_duplicates():
    s = Solution()
    nums = [1, 1, 2]
    k = s.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]
