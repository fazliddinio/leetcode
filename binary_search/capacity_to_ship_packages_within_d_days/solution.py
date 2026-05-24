"""
Capacity To Ship Packages Within D Days
LeetCode 1011

Approach: Binary Search on Answer
Time: O(n * log(sum(weights))) — binary search over capacity range
Space: O(1) — constant variable space
Brute: O(n * sum(weights)) — linear search starting from max(weights)
"""

from typing import List


class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            days_needed = 1
            current_load = 0
            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = weight
                else:
                    current_load += weight
            return days_needed <= days
            
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left
