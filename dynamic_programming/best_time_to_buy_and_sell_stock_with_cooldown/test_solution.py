import pytest
from .solution import Solution

def test_max_profit():
    s = Solution()
    assert s.maxProfit([1,2,3,0,2]) == 3
    assert s.maxProfit([1]) == 0
