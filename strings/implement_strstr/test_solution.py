import pytest
from .solution import Solution, SolutionBruteForce, SolutionBuiltIn

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionBuiltIn])
@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("a", "a", 0),
        ("mississippi", "issip", 4),
    ],
)
def test_str_str(SolutionClass, haystack, needle, expected):
    solution = SolutionClass()
    assert solution.strStr(haystack, needle) == expected
