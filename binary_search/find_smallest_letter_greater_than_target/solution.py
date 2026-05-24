"""
Find Smallest Letter Greater Than Target
LeetCode 744

Approach: Binary Search
Time: O(log n) — find smallest element > target in sorted array
Space: O(1) — constant variable space
Brute: O(n) — linear scan for first letter greater than target
"""

from typing import List


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
            
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left] if left < len(letters) else letters[0]
