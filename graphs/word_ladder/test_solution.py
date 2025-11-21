import pytest
from .solution import Solution

def test_ladder_length():
    s = Solution()
    assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
