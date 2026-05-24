"""
==========================================
  Subsets II (LeetCode 90)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array `nums` that may contain duplicates, return all
possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution
in any order.

Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Same as Subsets, but the input can have DUPLICATES. We must avoid
duplicate subsets.

    nums = [1, 2, 2]

    Without duplicates handling: [], [1], [2], [1,2], [2], [1,2], [2,2], [1,2,2]
                                              ↑ duplicate!  ↑ duplicate!

    Correct answer: [], [1], [2], [1,2], [2,2], [1,2,2]

How to avoid duplicates:
  1. SORT the array first: [1, 2, 2]
  2. When iterating at the same level, if nums[i] == nums[i-1], SKIP it.

    Sorted: [1, 2, 2]

    Index 0 (pick 1):  [1]
      Index 1 (pick 2): [1,2]
        Index 2 (pick 2): [1,2,2] ✓
      Index 2 (pick 2): SKIP! Same as index 1 at this level.
    Index 1 (pick 2):  [2]
      Index 2 (pick 2): [2,2] ✓
    Index 2 (pick 2):  SKIP! Same as index 1 at this level.

    Result: [], [1], [1,2], [1,2,2], [2], [2,2]
"""
