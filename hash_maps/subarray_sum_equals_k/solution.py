"""
Subarray Sum Equals K
LeetCode 560

Approach: Prefix Sum Map
Time: O(n) — Single pass.
Space: O(n) — Map stores unique prefix sums.
Brute: O(n^2) — Check all subarrays by computing each sum.
"""

from typing import List
from collections import defaultdict


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        for num in nums:
            prefix_sum += num
            count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1
        return count
