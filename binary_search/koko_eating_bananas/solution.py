"""
Koko Eating Bananas
LeetCode 875

Approach: Binary Search on Answer
Time: O(n log m) — n=piles, m=max(piles)
Space: O(1) — constant variable space
Brute: O(n * m) — try every speed from 1 to max(piles) linearly
"""

from typing import List
import math


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        
        while left <= right:
            mid = left + (right - left) // 2
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / mid)
                
            if hours_needed <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
