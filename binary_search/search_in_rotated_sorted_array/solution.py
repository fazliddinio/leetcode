"""
Search in Rotated Sorted Array
LeetCode 33

Approach: Modified Binary Search
Time: O(log n) — standard BS complexity adjusting for rotation
Space: O(1) — constant variable space
Brute: O(n) — linear scan through the array
"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
                
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1
