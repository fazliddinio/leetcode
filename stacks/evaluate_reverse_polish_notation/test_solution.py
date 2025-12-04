import pytest
from .solution import Solution, SolutionRecursive

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionRecursive])
@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_eval_rpn(SolutionClass, tokens, expected):
    solution = SolutionClass()
    # Recursive solution modifies the list (pop). So we need a copy.
    tokens_copy = list(tokens)
    assert solution.evalRPN(tokens_copy) == expected
