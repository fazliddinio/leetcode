import pytest
from .solution import Solution, SolutionReverse

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionReverse])
@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
    ],
)
def test_is_palindrome(SolutionClass, s, expected):
    solution = SolutionClass()
    assert solution.isPalindrome(s) == expected
