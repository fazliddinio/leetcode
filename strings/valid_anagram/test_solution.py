import pytest
from .solution import Solution, SolutionSorting, SolutionArray

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionSorting, SolutionArray])
@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "b", False),
        ("", "", True),
    ],
)
def test_is_anagram(SolutionClass, s, t, expected):
    solution = SolutionClass()
    assert solution.isAnagram(s, t) == expected
