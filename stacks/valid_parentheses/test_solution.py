import pytest
from .solution import Solution, SolutionReplace

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionReplace])
@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
    ],
)
def test_valid_parentheses(SolutionClass, s, expected):
    solution = SolutionClass()
    assert solution.isValid(s) == expected
