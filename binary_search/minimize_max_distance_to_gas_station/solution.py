"""
Minimize Max Distance to Gas Station
LeetCode 774

Approach: Binary Search on Answer
Time: O(n log(max_dist / epsilon)) — binary search over float range
Space: O(1) — constant variable space
Brute: O(K log n) — greedily add stations to max segment using a heap
"""

from typing import List
import math


class Solution:

    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(mid: float) -> bool:
            count = 0
            for i in range(len(stations) - 1):
                gap = stations[i + 1] - stations[i]
                count += math.ceil(gap / mid) - 1
            return count <= k
            
        left, right = 0.0, stations[-1] - stations[0]
        epsilon = 1e-06
        
        while right - left > epsilon:
            mid = (left + right) / 2.0
            if possible(mid):
                right = mid
            else:
                left = mid
                
        return left
