"""
Longest Consecutive Sequence
LeetCode 128

Approach: Hash Set
Time: O(n) — Each number visited at most twice.
Space: O(n) — Store all numbers in set.
Brute: O(n log n) — Sort and scan for consecutive runs.
"""

from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                longest = max(longest, current_length)
        return longest
