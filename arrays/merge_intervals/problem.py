"""
==========================================
  Merge Intervals (LeetCode 56)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    - 1 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^4


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

You have a bunch of time ranges. Some overlap. Combine the overlapping ones.

    Input:  [1,3], [2,6], [8,10], [15,18]

    [1,3] and [2,6] overlap (3 >= 2) → merge to [1,6]
    [8,10] doesn't overlap with [1,6] (8 > 6) → keep separate
    [15,18] doesn't overlap with [8,10] → keep separate

    Output: [1,6], [8,10], [15,18]

Strategy:
    1. Sort intervals by start time
    2. Walk through: if current interval overlaps with the last merged one,
       extend the end. Otherwise, start a new group.

    Think of it like a timeline:
    ───[1━━━3]──────
    ─────[2━━━━━6]──
    ════[1━━━━━━6]══  ← merged!
"""
