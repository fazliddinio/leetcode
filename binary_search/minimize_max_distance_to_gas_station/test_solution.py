import pytest
from .solution import Solution

def test_minmax_gas_dist():
    s = Solution()
    # Approx check for float result
    assert abs(s.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) - 0.5) < 1e-6
    assert abs(s.minmaxGasDist([23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1) - 14.0) < 1e-6
