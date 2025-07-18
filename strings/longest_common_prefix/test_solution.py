import pytest
from .solution import Solution

def test_longest_common_prefix():
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert s.longestCommonPrefix(["a"]) == "a"
