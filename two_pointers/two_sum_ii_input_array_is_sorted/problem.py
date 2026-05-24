"""
==========================================
  Two Sum II - Input Array Is Sorted (LeetCode 167)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1: Input: numbers = [2,7,11,15], target = 9, Output: [1,2]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Just like Two Sum, but the array is sorted, AND we must use O(1) Memory (No Hash Maps!)
*Note: The answer wants 1-based indices.*

Method: Two Pointers (Inward)
  Put a Left pointer at index 0 and a Right pointer at the end.
  Check `sum = nums[L] + nums[R]`.
  If it equals target -> Boom! Return `[L+1, R+1]`.
  If `sum > target` -> The sum is too big! We must decrease it. Move the Right pointer down.
  If `sum < target` -> The sum is too small! We must increase it. Move the Left pointer up.
"""
