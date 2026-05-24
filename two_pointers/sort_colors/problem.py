"""
==========================================
  Sort Colors (LeetCode 75)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1: Input: nums = [2,0,2,1,1,0], Output: [0,0,1,1,2,2]
Example 2: Input: nums = [2,0,1], Output: [0,1,2]

Constraints: n == nums.length, 1 <= n <= 300, nums[i] is either 0, 1, or 2.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Sort an array that only contains 0s, 1s, and 2s.
You must do this in a SINGLE pass without allocating extra memory!

Method: Dutch National Flag Algorithm (3 Pointers)
  We use three pointers: `low`, `mid`, and `high`.
  - `low` tracks where the next `0` should go.
  - `high` tracks where the next `2` should go.
  - `mid` scans the array.

  If nums[mid] == 0:
      Swap nums[low] and nums[mid].
      Move BOTH low and mid forward. (Because data coming from 'low' is already processed or is 1).
  If nums[mid] == 1:
      Just move mid forward.
  If nums[mid] == 2:
      Swap nums[mid] and nums[high].
      Move high backward.
      Do NOT move mid! (Because the data swapped in from 'high' is unknown and must be evaluated).
"""
