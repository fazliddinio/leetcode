# LeetCode 213: House Robber II
# Time: O(n), Space: O(1)

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_range(start, end):
            rob1, rob2 = 0, 0
            for i in range(start, end):
                rob1, rob2 = rob2, max(rob1 + nums[i], rob2)
            return rob2
        
        return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))
