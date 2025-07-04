# LeetCode 217: Contains Duplicate
# Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
