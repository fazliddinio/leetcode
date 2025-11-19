# 560. Subarray Sum Equals K
# Time: O(n)  – single pass prefix sum
# Space: O(n) – hash map of prefix counts
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = 0
        cnt = defaultdict(int, {0: 1})
        res = 0
        for v in nums:
            pref += v
            res += cnt[pref - k]
            cnt[pref] += 1
        return res