import pytest
from .solution import Solution

def test_contains_duplicate():
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) == True
    assert s.containsDuplicate([1, 2, 3, 4]) == False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True