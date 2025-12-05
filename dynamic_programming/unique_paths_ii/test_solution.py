import pytest
from .solution import Solution

def test_unique_paths_with_obstacles():
    s = Solution()
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    assert s.uniquePathsWithObstacles(grid) == 2
    
    grid = [[0,1],[0,0]]
    assert s.uniquePathsWithObstacles(grid) == 1
