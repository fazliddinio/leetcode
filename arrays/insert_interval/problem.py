"""
==========================================
  Insert Interval (LeetCode 57)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given an array of non-overlapping intervals `intervals` where
intervals[i] = [start_i, end_i] represent the start and the end of the i-th
interval and intervals is sorted in ascending order by start_i. You are also
given an interval newInterval = [start, end] that represents the start and end
of another interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by start_i and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new
array and return it.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: The new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    - 0 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^5
    - intervals is sorted by start_i in ascending order.
    - newInterval.length == 2
    - 0 <= start <= end <= 10^5


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

You have a sorted schedule of meetings that don't overlap, and you want to
add a new meeting. It might overlap and merge with existing ones!

    Schedule: [1-3], [6-9]
    New Meeting: [2-5]

    [1-3] and [2-5] overlap! → Merge to [1-5]
    [6-9] doesn't overlap → Keep as is
    Result: [1-5], [6-9]

Three-phase approach:
    Phase 1: Add all intervals that END before newInterval starts (no overlap)
    Phase 2: Merge all intervals that OVERLAP with newInterval
    Phase 3: Add all remaining intervals (they start after newInterval ends)

    intervals:    [1,3]  [6,9]
    newInterval:       [2,5]

    Phase 1: [1,3] ends at 3 >= 2 (start of new) → NOT before. Skip to Phase 2.
    Phase 2: [1,3] overlaps [2,5] → merged = [1,5]. [6,9] starts at 6 > 5 → stop.
    Phase 3: Add [6,9].
    Result: [[1,5], [6,9]]
"""
