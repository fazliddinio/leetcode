"""
Non-overlapping Intervals
LeetCode 435

Approach: Greedy (Sort by End Time)
Time: O(N log N) — sorting
Space: O(1) — constant extra space (ignoring sort stack)
Brute: O(2^N) — try all subsets to find max non-overlapping set
"""

from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]
        return len(intervals) - count
