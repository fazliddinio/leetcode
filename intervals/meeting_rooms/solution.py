"""
Meeting Rooms
LeetCode 252

Approach: Sort
Time: O(N log N) — sorting intervals
Space: O(1) — in-place sort (or O(N) depends on sort implementation)
Brute: O(N^2) — check all pairs for overlap
"""

from typing import List


class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
