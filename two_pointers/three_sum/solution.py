"""
3Sum
LeetCode 15

Approach: Sort + Two Pointers
Time: O(n²) — sorting O(n log n) + nested loop O(n²)
Space: O(1) — excluding output
Brute: O(n²) — for each element, use hash set to find two-sum complement
"""

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            target = -nums[i]
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
