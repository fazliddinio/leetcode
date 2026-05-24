"""
Search in Rotated Sorted Array II
LeetCode 81

Approach: Modified Binary Search with Duplicate Handling
Time: O(n) worst case, O(log n) average — worst case when all elements are same
Space: O(1) — constant extra space
Brute: O(n) — linear scan through the array
"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
                
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
