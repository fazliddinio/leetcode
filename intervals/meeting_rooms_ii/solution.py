"""
Meeting Rooms II
LeetCode 253

Approach: Min-Heap
Time: O(N log N) — sorting + heap operations
Space: O(N) — heap stores end times
Brute: O(N log N) — chronological event sweep with start/end pointers
"""

from typing import List
import heapq


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, intervals[i][1])
        return len(free_rooms)
