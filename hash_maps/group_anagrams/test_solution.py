import pytest
from .solution import Solution

def test_group_anagrams():
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = s.groupAnagrams(strs)
    # Sort groups for comparison
    result = sorted([sorted(g) for g in result])
    expected = sorted([sorted(["bat"]), sorted(["nat","tan"]), sorted(["ate","eat","tea"])])
    assert result == expected

    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
