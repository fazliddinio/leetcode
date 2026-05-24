"""
Merge Intervals
LeetCode 56

Approach: Sort + Linear Merge
Time: O(n log n) — sorting dominates
Space: O(n) — output list
Brute: O(n²) — repeatedly merge overlapping pairs until stable
"""

from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            last = merged[-1]
            curr = intervals[i]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)
        return merged
