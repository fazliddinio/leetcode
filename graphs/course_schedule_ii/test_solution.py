import pytest
from .solution import Solution

def test_find_order():
    s = Solution()
    assert s.findOrder(2, [[1,0]]) == [0, 1]
    assert s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in [[0,1,2,3], [0,2,1,3]]
    assert s.findOrder(1, []) == [0]
