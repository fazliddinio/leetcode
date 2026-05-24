"""
Happy Number
LeetCode 202

Approach: Floyd's Cycle Detection
Time: O(log n) — sum of squares decreases rapidly
Space: O(1) — constant extra space
Brute: O(log n) — use hash set to detect cycles using O(log n) space
"""


class Solution:

    def get_next(self, num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return fast == 1
