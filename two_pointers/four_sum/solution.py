"""
4Sum
LeetCode 18

Approach: Sort + K-Sum recursive generalization
Time: O(n³) — for k=4, reduces to O(n^(k-1))
Space: O(n) — recursion stack space and sorting
Brute: O(n³) — two nested loops + two-pointer scan (iterative approach)
"""

from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if not nums:
                return res

            average_value = target // k
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            left, right = 0, len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                elif curr_sum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
