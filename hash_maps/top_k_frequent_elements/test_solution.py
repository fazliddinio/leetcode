import pytest
from .solution import Solution

def test_top_k_frequent():
    s = Solution()
    # Order doesn't strictly matter if frequency is same, 
    # but for unique frequencies it's deterministic.
    # The problem says answer is unique.
    assert sorted(s.topKFrequent([1,1,1,2,2,3], 2)) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
