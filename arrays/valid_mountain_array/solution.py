"""
Valid Mountain Array
LeetCode 941

Approach: One Pass (Climb Up then Down)
Time: O(n) — single pass from left to right
Space: O(1) — constant extra space
Brute: O(n) — find max element, verify increasing before and decreasing after
"""

from typing import List


class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        """One Pass Approach"""
        if len(arr) < 3:
            return False
        n = len(arr)
        i = 0
        
        # Climb up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
            
        # Peak cannot be the first or last element
        if i == 0 or i == n - 1:
            return False
            
        # Climb down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
            
        return i == n - 1
