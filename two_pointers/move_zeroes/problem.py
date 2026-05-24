"""
==========================================
  Move Zeroes (LeetCode 283)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1: Input: nums = [0,1,0,3,12], Output: [1,3,12,0,0]
Example 2: Input: nums = [0], Output: [0]

Constraints: 1 <= nums.length <= 10^4, -2^31 <= nums[i] <= 2^31 - 1

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Take all the zeroes in the array and shove them to the back, but keep the other numbers in their original order.
Don't create a new array!

    nums = [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]

Method: Two Pointers (Snowball/Write Pointer)
  Use one pointer `L` (the "write" pointer) to track where the next non-zero number should go.
  Use another pointer `R` (the "read" pointer) to scan through the array.

  If nums[R] is completely normal (not zero):
      Swap nums[L] and nums[R]!
      Move L forward.

    L,R
    [0, 1, 0, 3, 12]  -> R points to 0. Ignore.

    L   R
    [0, 1, 0, 3, 12]  -> R points to 1. Swap L (0) and R (1)! Move L.
    [1, 0, 0, 3, 12]

        L   R
    [1, 0, 0, 3, 12]  -> R points to 0. Ignore.

        L       R
    [1, 0, 0, 3, 12]  -> R points to 3. Swap L and R! Move L.
    [1, 3, 0, 0, 12]
"""
