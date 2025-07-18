import pytest
from .solution import Solution

def test_is_anagram():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False
    assert s.isAnagram("", "") == True
