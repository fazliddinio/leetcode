import pytest
from .solution import Solution

def test_valid_tree():
    s = Solution()
    assert s.validTree(5, [[0,1], [0,2], [0,3], [1,4]]) == True
    assert s.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]) == False
