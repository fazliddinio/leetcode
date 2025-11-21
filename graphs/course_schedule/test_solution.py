import pytest
from .solution import Solution

def test_can_finish():
    s = Solution()
    assert s.canFinish(2, [[1,0]]) == True
    assert s.canFinish(2, [[1,0],[0,1]]) == False
