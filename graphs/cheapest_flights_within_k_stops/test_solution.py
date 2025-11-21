import pytest
from .solution import Solution

def test_find_cheapest_price():
    s = Solution()
    assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
    assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500
