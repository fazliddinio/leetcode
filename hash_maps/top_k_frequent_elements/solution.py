# 347. Top K Frequent Elements
# Time: O(n)  – single pass + bucket sort
# Space: O(n) – buckets and hash map
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for v in nums:
            freq[v] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for v, c in freq.items():
            bucket[c].append(v)
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            ans.extend(bucket[i])
            if len(ans) >= k:
                return ans[:k]
        return ans