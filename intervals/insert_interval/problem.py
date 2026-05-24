"""
==========================================
  Insert Interval (LeetCode 57)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given an array of non-overlapping intervals `intervals` where intervals[i] = [start_i, end_i] represent the start and the end of the i-th interval and intervals is sorted in ascending order by start_i. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by start_i and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Example 1: Input: intervals = [[1,3],[6,9]], newInterval = [2,5], Output: [[1,5],[6,9]]
Example 2: Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8], Output: [[1,2],[3,10],[12,16]]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
You have a schedule of meetings that don't overlap, and you want to add a new meeting. It might overlap and merge with existing ones!

    Schedule: [1-3], [6-9]
    New Meeting: [2-5]

    [1-3] and [2-5] overlap! -> Merge to [1-5]
    [6-9] doesn't overlap. Next!
    Result: [1-5], [6-9]

Method:
  Step 1: Loop while the endpoints of intervals are BEFORE the start of `newInterval`. Add them to output.
  Step 2: While the intervals OVERLAP with `newInterval`, merge them (update `newInterval` bounds).
          `newInterval` = [min start, max end]
          Add the massive merged `newInterval` to output!
  Step 3: Add whatever is left from the original intervals.
"""
