"""
==========================================
  Squares of a Sorted Array (LeetCode 977)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1: Input: nums = [-4,-1,0,3,10], Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

Constraints: 1 <= nums.length <= 10^4, -10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Square every number in an array, then sort it. But do it in O(n) time!
The tricky part is that negative numbers become positive when squared, so `-4` becomes bigger than `3`.

Method: Two Pointers (From the outside in!)
  Because the input is sorted, the BIGGEST square will ALWAYS be at the very edges (the most negative number, or the most positive number).
  1. Create a result array of the same size.
  2. Put a pointer at the start `L` and end `R`.
  3. Compare `nums[L]^2` and `nums[R]^2`.
  4. Whichever is bigger, drop it at the END of the result array.
  5. Move the pointer inward, and repeat!
"""
