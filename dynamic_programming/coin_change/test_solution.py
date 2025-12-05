import pytest
from .solution import Solution

def test_coin_change():
    s = Solution()
    assert s.coinChange([1,2,5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
