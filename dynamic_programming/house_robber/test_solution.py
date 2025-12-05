import pytest
from .solution import Solution

def test_rob():
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12
