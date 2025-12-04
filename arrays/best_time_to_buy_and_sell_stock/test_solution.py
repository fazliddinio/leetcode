import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([], 0),
        ([2, 4, 1], 2),
    ],
)
def test_max_profit(SolutionClass, prices, expected):
    solution = SolutionClass()
    assert solution.maxProfit(prices) == expected