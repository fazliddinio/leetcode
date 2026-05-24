"""
Daily Temperatures
LeetCode 739

Approach: Monotonic Decreasing Stack
Time: O(n) — Single pass.
Space: O(n) — Stack storage.
Brute: O(n^2) — For each day, scan forward for a warmer day.
"""

from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)
        return result
