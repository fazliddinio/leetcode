"""
==========================================
  Four Sum (LeetCode 18)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1: Input: nums = [1,0,-1,0,-2,2], target = 0, Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find every unique combo of 4 numbers that sum to the target!

    nums = [1, 0, -1, 0, -2, 2], target = 0
    [-2, -1, 1, 2] equals 0!

Method: Sort + Two Pointers (Nested Loops)
  Just like 3Sum, but add one more loop on the outside!
  1. Sort the array so we can use Two Pointers.
  2. Iterate `i` from 0 to n-3. (Skip duplicate values of `nums[i]`)
  3. Inside, iterate `j` from i+1 to n-2. (Skip duplicate values of `nums[j]`)
  4. Now do standard Two Pointers! `left` at j+1, `right` at n-1.
  5. If `nums[i] + nums[j] + nums[left] + nums[right] < target` -> move left up.
  6. If `... > target` -> move right down.
  7. If equal, record it! and skip duplicate lefts/rights.
"""
