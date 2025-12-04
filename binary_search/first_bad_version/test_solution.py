import pytest
from .solution import Solution, SolutionBruteForce
import sys
from unittest.mock import patch

# Mocking isBadVersion globally for the solution module might be tricky if it imports it, 
# but here it uses global scope or argument injection?
# The solution expects `isBadVersion` in globals().
# We can patch it in the test module, but the solution module imports it or expects it.
# Actually, the solution file defines a dummy if not in globals.
# Use `unittest.mock.patch` on the module where Solution is defined.

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "n, bad, expected",
    [
        (5, 4, 4),
        (1, 1, 1),
        (100, 50, 50),
    ],
)
def test_first_bad_version(SolutionClass, n, bad, expected):
    # We need to inject isBadVersion into the solution module namespace
    # or patch it.
    
    def mock_isBadVersion(version):
        return version >= bad
        
    with patch('leetcode.binary_search.first_bad_version.solution.isBadVersion', side_effect=mock_isBadVersion):
        solution = SolutionClass()
        assert solution.firstBadVersion(n) == expected
