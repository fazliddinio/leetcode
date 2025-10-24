import pytest
from .solution import Solution

def test_search():
    s = Solution()
    assert s.search([-1,0,3,5,9,12], 9) == 4
    assert s.search([-1,0,3,5,9,12], 2) == -1
    assert s.search([5], 5) == 0
