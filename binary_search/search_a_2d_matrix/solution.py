"""
Search a 2D Matrix
LeetCode 74

Approach: Binary Search (treat as 1D array)
Time: O(log(m * n)) — true binary search over all elements
Space: O(1) — constant variable space
Brute: O(m + n) — step-wise search from top-right corner
"""

from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
