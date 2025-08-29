import pytest
from .solution import Solution

def test_check_inclusion():
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("ab", "eidboaoo") == False
