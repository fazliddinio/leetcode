"""
==========================================
  Maximum Average Subarray I (LeetCode 643)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Example 1: Input: nums = [1,12,-5,-6,50,3], k = 4, Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Slide a window of exactly size `K` across the array and find the one with the biggest sum (and therefore biggest average).

Method: Fixed Sliding Window
  1. Calculate the sum of the very first `K` elements. Initialize `max_sum = current_sum`.
  2. Slide the window one step:
     - Subtract `nums[i - k]` (the element falling out of the window).
     - Add `nums[i]` (the new element entering the window).
  3. Update `max_sum = max(max_sum, current_sum)`.
  4. Return `max_sum / k`.
"""
