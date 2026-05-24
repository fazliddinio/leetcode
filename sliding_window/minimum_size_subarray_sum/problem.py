"""
==========================================
  Minimum Size Subarray Sum (LeetCode 209)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1: Input: target = 7, nums = [2,3,1,2,4,3], Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Constraints: 1 <= target <= 10^9, 1 <= nums.length <= 10^5, 1 <= nums[i] <= 10^4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the absolutely shortest slice of the array whose sum is AT LEAST the target.

Method: Sliding Window
  1. Add numbers to your window sum by moving `Right` forward.
  2. While the current sum >= target:
     - You found a valid slice! Record its length `Right - Left + 1` if it's the lowest you've seen.
     - Now, try to make it even SHORTER by removing the leftmost element.
     - Move `Left` forward and subtract from sum!
"""
