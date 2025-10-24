import pytest
from .solution import Solution

def test_search():
    s = Solution()
    assert s.search([2,5,6,0,0,1,2], 0) == True
    assert s.search([2,5,6,0,0,1,2], 3) == False
