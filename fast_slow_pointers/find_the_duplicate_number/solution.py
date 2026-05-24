"""
Find the Duplicate Number
LeetCode 287

Approach: Floyd's Tortoise and Hare
Time: O(n) — linear time cycle detection
Space: O(1) — no extra space
Brute: O(n log n) — binary search on value range using pigeonhole principle
"""

from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
