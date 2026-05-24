import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_isPalindrome_example1(solution):
    s = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s) is True
    assert solution.isPalindrome_reverse(s) is True

def test_isPalindrome_example2(solution):
    s = "race a car"
    assert solution.isPalindrome(s) is False
    assert solution.isPalindrome_reverse(s) is False

def test_isPalindrome_empty(solution):
    s = " "
    assert solution.isPalindrome(s) is True
    assert solution.isPalindrome_reverse(s) is True

def test_isPalindrome_numbers(solution):
    s = "0P"
    assert solution.isPalindrome(s) is False
    assert solution.isPalindrome_reverse(s) is False
