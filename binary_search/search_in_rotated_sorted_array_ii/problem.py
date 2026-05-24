"""
==========================================
  Search in Rotated Sorted Array II (LeetCode 81)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

There is an integer array `nums` sorted in non-decreasing order (not
necessarily with distinct values). Before being passed to your function,
nums is rotated at an unknown pivot index k.

Given the array `nums` after the rotation and an integer `target`, return
`true` if target is in nums, or `false` if it is not.

This is a follow-up to Search in Rotated Sorted Array, where nums may
contain duplicates.

Example 1:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true

Example 2:
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false

Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - nums may contain duplicates.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Same as Search in Rotated Sorted Array, but now DUPLICATES are allowed.

    [2, 5, 6, 0, 0, 1, 2]    target = 0

The problem with duplicates:
    [1, 0, 1, 1, 1]   nums[left]=1, nums[mid]=1, nums[right]=1
    We can't tell which side is sorted!

Solution: When nums[left] == nums[mid] == nums[right],
           just shrink both ends: left++, right--

    After shrinking: [0, 1, 1]  → now we can binary search normally.

Worst case: O(n) if all elements are the same.
Average case: still O(log n).
"""
