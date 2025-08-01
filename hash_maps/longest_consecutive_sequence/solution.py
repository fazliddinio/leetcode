# LeetCode 128: Longest Consecutive Sequence
# Time: O(n), Space: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for n in num_set:
            if n - 1 not in num_set:  # start of sequence
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest