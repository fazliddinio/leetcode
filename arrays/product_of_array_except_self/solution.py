# LeetCode 238: Product of Array Except Self
# Time: O(n), Space: O(1) excluding output

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        
        # left pass
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # right pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result