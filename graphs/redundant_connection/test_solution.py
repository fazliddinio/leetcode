import pytest
from .solution import Solution

def test_find_redundant_connection():
    s = Solution()
    assert s.findRedundantConnection([[1,2], [1,3], [2,3]]) == [2, 3]
    assert s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]) == [1, 4]
