import pytest
from unittest.mock import patch
from .solution import Solution

def test_first_bad_version():
    # Patch the isBadVersion in the solution module
    with patch('leetcode.binary_search.first_bad_version.solution.isBadVersion') as mock_is_bad:
        s = Solution()
        
        # Case 1: n=5, bad=4
        mock_is_bad.side_effect = lambda v: v >= 4
        assert s.firstBadVersion(5) == 4
        
        # Case 2: n=1, bad=1
        mock_is_bad.side_effect = lambda v: v >= 1
        assert s.firstBadVersion(1) == 1
