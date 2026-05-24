"""
Min Cost Climbing Stairs
LeetCode 746

Approach: Space Optimized DP
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(2^n) — Recurse trying 1 or 2 steps from each position without memoization.
"""

from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = cost[0]
        second = cost[1]
        if n <= 2:
            return min(first, second)
        for i in range(2, n):
            current = cost[i] + min(first, second)
            first = second
            second = current
        return min(first, second)
