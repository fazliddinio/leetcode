# LeetCode 347: Top K Frequent Elements
# Time: O(n), Space: O(n)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]
        return result