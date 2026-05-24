"""
Plus One
LeetCode 66

Approach: Iteration from End
Time: O(n) — single pass through digits in worst case
Space: O(1) — in-place modification
Brute: O(n) — convert to string, add one, convert back to list
"""

from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        """Iteration from End Approach"""
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
