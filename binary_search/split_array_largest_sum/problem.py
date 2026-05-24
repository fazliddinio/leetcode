"""
==========================================
  Split Array Largest Sum (LeetCode 410)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array `nums` and an integer `k`, split `nums` into `k`
non-empty subarrays such that the largest sum of any subarray is
minimized.

Return the minimized largest sum of the split.

Example 1:
    Input: nums = [7,2,5,10,8], k = 2
    Output: 18
    Explanation: Split into [7,2,5] and [10,8].
                 The largest sum is max(14, 18) = 18, which is minimized.

Example 2:
    Input: nums = [1,2,3,4,5], k = 2
    Output: 9

Constraints:
    - 1 <= nums.length <= 1000
    - 0 <= nums[i] <= 10^6
    - 1 <= k <= min(50, nums.length)


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Split an array into k groups. The "cost" is the largest group sum.
Minimize that cost.

    nums = [7, 2, 5, 10, 8]    k = 2

    Option A: [7,2,5] | [10,8]  →  sums: 14, 18  → max = 18
    Option B: [7,2] | [5,10,8]  →  sums: 9, 23   → max = 23
    Option C: [7] | [2,5,10,8]  →  sums: 7, 25   → max = 25

    Best: Option A with max = 18  ★

Binary search on the ANSWER (the max sum S):
    Low = max(nums) = 10  (each group has at least one element)
    High = sum(nums) = 32 (one group has everything)

    "Can we split into ≤ k groups with each group sum ≤ S?"

    S=21 → greedily pack: [7,2,5] (14) | [10,8] (18) → 2 groups ≤ 2 ✓
    S=15 → [7,2,5] (14) | [10] (10) | [8] (8) → 3 groups > 2 ✗
    S=18 → [7,2,5] (14) | [10,8] (18) → 2 groups ≤ 2 ✓
    S=16 → [7,2,5] (14) | [10] (10) | [8] → 3 groups > 2 ✗
    S=17 → [7,2,5] (14) | [10] (10) | [8] → 3 groups > 2 ✗
    → Answer: 18  ★
"""
