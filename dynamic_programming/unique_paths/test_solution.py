import pytest
from .solution import Solution

def test_unique_paths():
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
