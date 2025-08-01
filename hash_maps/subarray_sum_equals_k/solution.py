# LeetCode 560: Subarray Sum Equals K
# Time: O(n), Space: O(n)

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = {0: 1}
        
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
        
        return count