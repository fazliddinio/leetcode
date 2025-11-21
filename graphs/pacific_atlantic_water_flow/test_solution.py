import pytest
from .solution import Solution

def test_pacific_atlantic():
    s = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    res = s.pacificAtlantic(heights)
    
    expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    # Sort for comparison
    assert sorted([list(x) for x in res]) == sorted([list(x) for x in expected])
