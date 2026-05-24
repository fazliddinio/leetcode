"""
Two Sum II - Input Array Is Sorted
LeetCode 167

Approach: Two Pointers
Time: O(n) — single pass from both ends
Space: O(1) — constant variable space
Brute: O(n log n) — for each element, binary search for complement
"""

from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
