import pytest
from .solution import Solution

def test_search_matrix():
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert s.searchMatrix(matrix, 3) == True
    assert s.searchMatrix(matrix, 13) == False
