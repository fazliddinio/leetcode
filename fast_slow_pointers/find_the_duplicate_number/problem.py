"""
==========================================
  Find the Duplicate Number (LeetCode 287)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1: Input: nums = [1,3,4,2,2], Output: 2

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the only duplicate number in an array, BUT you can't modify the array, use `sort()`, or use a Hash Set. Time O(n) Space O(1).

Method: Fast & Slow Pointers (Floyd's Tortoise and Hare)
  Treat the array values as "Next Pointers".
  Index 0 -> Value 1 (Go to index 1)
  If there is a duplicate number, multiple indices point to the SAME index! This creates a CYCLE.
  
  1. Run Fast and Slow pointers until they intersect inside the cycle.
  2. Reset Slow to the beginning.
  3. Move both at the same speed. Where they intersect is the entrance to the cycle (the duplicate number!).
"""
