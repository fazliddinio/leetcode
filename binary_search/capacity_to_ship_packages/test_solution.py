import pytest
from .solution import Solution

def test_ship_within_days():
    s = Solution()
    assert s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5) == 15
    assert s.shipWithinDays([3,2,2,4,1,4], 3) == 6
    assert s.shipWithinDays([1,2,3,1,1], 4) == 3
