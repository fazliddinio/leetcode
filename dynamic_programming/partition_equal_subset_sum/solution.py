"""
Partition Equal Subset Sum
LeetCode 416

Approach: DP / Set
Time: O(N * S) — Worst case sum is N*max_val. With bitset/set optimization it's faster but bounded by sum.
Space: O(S) — Set to store reachable sums up to S/2.
Brute: O(2^n) — Recurse including or excluding each number to reach target sum.
"""

from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = {0}
        for num in nums:
            new_sums = set()
            for s in dp:
                if s + num == target:
                    return True
                if s + num < target:
                    new_sums.add(s + num)
            dp.update(new_sums)
        return target in dp
