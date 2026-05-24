"""
Longest Increasing Subsequence
LeetCode 300

Approach: Binary Search (Patience Sorting)
Time: O(N log N) — Iterate N elements, binary search takes log N.
Space: O(N) — Arrays to store tails.
Brute: O(N^2) — DP where dp[i] = LIS ending at index i, checking all previous elements.
"""

from typing import List
import bisect


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx < len(tails):
                tails[idx] = num
            else:
                tails.append(num)
        return len(tails)
