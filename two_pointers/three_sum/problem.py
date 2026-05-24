"""
==========================================
  3Sum (LeetCode 15)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1: Input: nums = [-1,0,1,2,-1,-4], Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find all groups of exactly three numbers that sum to ZERO. No duplicate groups allowed!

Method: Sort + Two Pointers
  1. Sort the entire array first. (O(n log n))
  2. Iterate `i` through the array. This `nums[i]` is our first number.
     - If `i > 0` and `nums[i] == nums[i-1]`, SKIP it to avoid duplicate groups!
  3. Now we need to find 2 numbers that sum to `-nums[i]`. This is just Two Sum II!
     - Use a `left` pointer at `i + 1` and a `right` pointer at `end`.
     - Check `sum = nums[i] + nums[left] + nums[right]`.
     - If `sum < 0`: Need more! `left += 1`.
     - If `sum > 0`: Too big! `right -= 1`.
     - If `sum == 0`: We found a match! Record it.
          Then `left += 1`.
          But also SKIP duplicate values of `nums[left]` so we don't return the same triplet twice!
"""
