"""
Climbing Stairs
LeetCode 70

Approach: Space Optimized DP
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(2^n) — Recurse trying 1 or 2 steps at each position without memoization.
"""

from typing import List


class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one_step_before = 2
        two_steps_before = 1
        for i in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        return one_step_before
