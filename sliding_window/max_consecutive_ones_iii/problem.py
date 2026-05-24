"""
==========================================
  Max Consecutive Ones III (LeetCode 1004)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1: Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2, Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1] (Flipped the last two 0s).

Constraints: 1 <= nums.length <= 10^5, nums[i] is either 0 or 1, 0 <= k <= nums.length

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the longest stretch of 1s you can get if you are allowed to magically turn up to `k` zeroes into ones!

Method: Sliding Window
  1. Window has a `Left` and `Right` pointer.
  2. Put `Right` down the array. If `nums[Right]` is 0, decrease `k`! (You just used a flip).
  3. If `k < 0` (you ran out of flips!):
     - The window is INVALID.
     - Move `Left` forward. If `nums[Left]` was a 0, you get your flip back! (`k += 1`)
  4. The size of the biggest valid window is `max(max_len, Right - Left + 1)`.
"""
