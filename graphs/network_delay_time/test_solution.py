import pytest
from .solution import Solution

def test_network_delay_time():
    s = Solution()
    assert s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    assert s.networkDelayTime([[1,2,1]], 2, 1) == 1
    assert s.networkDelayTime([[1,2,1]], 2, 2) == -1
