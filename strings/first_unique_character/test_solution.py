import pytest
from .solution import Solution

def test_first_uniq_char():
    s = Solution()
    assert s.firstUniqChar("leetcode") == 0
    assert s.firstUniqChar("loveleetcode") == 2
    assert s.firstUniqChar("aabb") == -1
