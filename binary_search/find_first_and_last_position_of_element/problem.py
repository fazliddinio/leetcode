"""
==========================================
  Find First and Last Position of Element in Sorted Array (LeetCode 34)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an array of integers `nums` sorted in non-decreasing order, find
the starting and ending position of a given `target` value.

If `target` is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - nums is a non-decreasing array.
    - -10^9 <= target <= 10^9


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

In a sorted array, find WHERE a number first appears and WHERE it last
appears.

    nums = [5, 7, 7, 8, 8, 10]    target = 8

    Indexes: 0  1  2  3  4  5
                      ↑  ↑
                    first last → [3, 4]

Use binary search TWICE:
    Search 1: Find the LEFTMOST 8 (first position)
    Search 2: Find the RIGHTMOST 8 (last position)

    Finding leftmost 8:
    [5, 7, 7, 8, 8, 10]
               ↑ mid=2 → nums[2]=7 < 8 → go right
    [8, 8, 10]
     ↑ mid=3 → nums[3]=8 == 8 → found, but keep going LEFT
    → first = 3

    Finding rightmost 8:
    [5, 7, 7, 8, 8, 10]
               ↑ mid=2 → nums[2]=7 < 8 → go right
    [8, 8, 10]
        ↑ mid=4 → nums[4]=8 == 8 → found, but keep going RIGHT
    → last = 4

    Answer: [3, 4]
"""
