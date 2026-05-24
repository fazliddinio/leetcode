"""
==========================================
  Find Minimum in Rotated Sorted Array (LeetCode 153)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Suppose an array of length n sorted in ascending order is rotated between
1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.

Given the sorted rotated array `nums` of unique elements, return the
minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1

Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0

Example 3:
    Input: nums = [11,13,15,17]
    Output: 11

Constraints:
    - n == nums.length
    - 1 <= n <= 5000
    - -5000 <= nums[i] <= 5000
    - All values are unique.
    - nums is sorted and rotated between 1 and n times.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

A sorted array was "rotated" (the end was moved to the front). Find the
smallest number.

    Original: [0, 1, 2, 4, 5, 6, 7]
    Rotated:  [4, 5, 6, 7, 0, 1, 2]
                          ↑ minimum!

The array looks like two sorted halves:

    7 |       ●
    6 |     ●
    5 |   ●
    4 | ●
    2 |               ●
    1 |             ●
    0 |           ●       ← minimum is at the "drop"

Binary search: Compare mid with right end.
    - If nums[mid] > nums[right] → min is in RIGHT half
    - If nums[mid] < nums[right] → min is in LEFT half (including mid)

    [4, 5, 6, 7, 0, 1, 2]
              ↑ mid=7, right=2
              7 > 2 → go right
    [0, 1, 2]
     ↑ mid=1, right=2
     1 < 2 → go left (include mid)
    [0, 1]
     ↑ mid=0, right=1
     0 < 1 → go left
    → Answer: 0
"""
