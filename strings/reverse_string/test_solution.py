import pytest
from .solution import Solution, SolutionRecursive, SolutionBuiltIn

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionRecursive, SolutionBuiltIn])
@pytest.mark.parametrize(
    "s, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a"], ["a"]),
        ([], []),
    ],
)
def test_reverse_string(SolutionClass, s, expected):
    solution = SolutionClass()
    s_copy = list(s)
    solution.reverseString(s_copy)
    assert s_copy == expected
