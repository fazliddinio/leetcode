"""
Longest Turbulent Subarray
LeetCode 978

Approach: Sliding Window / State Machine
Time: O(n) — single pass
Space: O(1) — constant variable space
Brute: O(n²) — check every subarray for turbulence
"""

from typing import List


class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """Sliding Window / State Machine Approach"""
        n = len(arr)
        if n < 2:
            return n
            
        left = 0
        max_len = 1
        prev_sign = 0
        
        if arr[1] > arr[0]:
            prev_sign = 1
            max_len = 2
        elif arr[1] < arr[0]:
            prev_sign = -1
            max_len = 2
        else:
            left = 1
            
        for right in range(2, n):
            current_diff = arr[right] - arr[right - 1]
            current_sign = 0
            
            if current_diff > 0:
                current_sign = 1
            elif current_diff < 0:
                current_sign = -1
                
            if current_sign == 0:
                left = right
                prev_sign = 0
            elif current_sign == -prev_sign:
                max_len = max(max_len, right - left + 1)
                prev_sign = current_sign
            else:
                left = right - 1
                max_len = max(max_len, 2)
                prev_sign = current_sign
                
        return max_len
