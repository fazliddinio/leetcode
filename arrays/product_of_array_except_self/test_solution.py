import pytest
from .solution import Solution, SolutionBruteForce, SolutionAlternative

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionAlternative])
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([1, 0], [0, 1]),
    ],
)
def test_product_except_self(SolutionClass, nums, expected):
    solution = SolutionClass()
    assert solution.productExceptSelf(nums) == expected
