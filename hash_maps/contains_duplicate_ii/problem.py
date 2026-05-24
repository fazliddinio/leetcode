"""
==========================================
  Contains Duplicate II (LeetCode 219)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1: Input: nums = [1,2,3,1], k = 3, Output: true
Example 2: Input: nums = [1,0,1,1], k = 1, Output: true
Example 3: Input: nums = [1,2,3,1,2,3], k = 2, Output: false

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Are there duplicate numbers that are close to each other (distance <= k)?

Method: Hash Map or Sliding Window!

Using a Hash Map:
  Walk through the array. For each number, check if we've seen it before.
  If we HAVE seen it, is `current_index - last_seen_index <= k`?
  If yes, return True!
  If no, update the number's last seen index to the current index.
"""
