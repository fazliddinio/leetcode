"""
Grumpy Bookstore Owner
LeetCode 1052

Approach: Fixed Sliding Window
Time: O(n) — single pass
Space: O(1) — constant variable space
Brute: O(n²) — try every window position, recompute total each time
"""

from typing import List


class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """Fixed Sliding Window Approach"""
        always_satisfied = 0
        for c, g in zip(customers, grumpy):
            if g == 0:
                always_satisfied += c
                
        current_extra = 0
        max_extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                current_extra += customers[i]
                
        max_extra = current_extra
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_extra += customers[i]
            if grumpy[i - minutes] == 1:
                current_extra -= customers[i - minutes]
            max_extra = max(max_extra, current_extra)
            
        return always_satisfied + max_extra
