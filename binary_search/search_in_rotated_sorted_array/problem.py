"""
==========================================
  Search in Rotated Sorted Array (LeetCode 33)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

There is an integer array `nums` sorted in ascending order (with distinct
values). Prior to being passed to your function, nums is possibly rotated
at an unknown pivot index k.

Given the array `nums` after the possible rotation and an integer
`target`, return the index of target if it is in nums, or -1 if it is
not.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - All values of nums are unique.
    - nums may be rotated at some pivot.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

A sorted array was rotated — find a target in O(log n).

    [4, 5, 6, 7, 0, 1, 2]    target = 0
     ← sorted →  ← sorted →
                  ↑ target here!

At each step of binary search, ONE half is always sorted:

    [4, 5, 6, 7, 0, 1, 2]   mid=7
     ↑ left     ↑ mid    ↑ right

    Left half [4,5,6,7]: sorted (nums[left] ≤ nums[mid])
    Is target in [4..7]? 0 is NOT → go right

    [0, 1, 2]   mid=1
    Left half [0,1]: sorted
    Is target in [0..1]? 0 IS → go left

    [0] → found at index 4!

Decision logic:
    If LEFT half is sorted:
        If target is in [left..mid] → go left
        Else → go right
    If RIGHT half is sorted:
        If target is in [mid..right] → go right
        Else → go left
"""
