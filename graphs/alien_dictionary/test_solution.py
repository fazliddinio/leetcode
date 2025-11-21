import pytest
from .solution import Solution

def test_alien_order():
    s = Solution()
    assert s.alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf"
    assert s.alienOrder(["z","x"]) == "zx"
    assert s.alienOrder(["z","x","z"]) == ""
