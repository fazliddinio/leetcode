# LeetCode 26: Remove Duplicates from Sorted Array
# Time: O(n), Space: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
