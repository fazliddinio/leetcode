import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_validPalindrome_example1(solution):
    s = "aba"
    assert solution.validPalindrome(s) is True
    assert solution.validPalindrome_optimized(s) is True

def test_validPalindrome_example2(solution):
    s = "abca"
    assert solution.validPalindrome(s) is True
    assert solution.validPalindrome_optimized(s) is True

def test_validPalindrome_example3(solution):
    s = "abc"
    assert solution.validPalindrome(s) is False
    assert solution.validPalindrome_optimized(s) is False

def test_validPalindrome_empty(solution):
    s = ""
    assert solution.validPalindrome(s) is True
    assert solution.validPalindrome_optimized(s) is True
    
def test_validPalindrome_already_palindrome(solution):
    s = "racecar"
    assert solution.validPalindrome(s) is True
    assert solution.validPalindrome_optimized(s) is True
