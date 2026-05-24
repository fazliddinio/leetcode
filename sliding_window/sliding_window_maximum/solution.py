"""
Sliding Window Maximum
LeetCode 239

Approach: Monotonic Decreasing Deque
Time: O(n) — each element added/removed at most once
Space: O(k) — deque size is at most k
Brute: O(n * k) — scan each window for maximum
"""

from typing import List
from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Monotonic Deque Approach"""
        q = deque()
        res = []
        for i, n in enumerate(nums):
            # Remove indices that are out of the current window
            if q and q[0] == i - k:
                q.popleft()
                
            # Maintain monotonic decreasing property
            while q and nums[q[-1]] <= n:
                q.pop()
                
            q.append(i)
            
            # Start appending to result once window is formed
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
