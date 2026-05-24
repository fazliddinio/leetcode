"""
==========================================
  Combination Sum II (LeetCode 40)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given a collection of candidate numbers (`candidates`) and a target number
(`target`), find all unique combinations in `candidates` where the
candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: [[1,2,2],[5]]

Constraints:
    - 1 <= candidates.length <= 100
    - 1 <= candidates[i] <= 50
    - 1 <= target <= 30


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Same as Combination Sum, but TWO key differences:
  1. Each number can only be used ONCE.
  2. The input may have DUPLICATES.

    candidates = [10, 1, 2, 7, 6, 1, 5],  target = 8

    Sort first: [1, 1, 2, 5, 6, 7, 10]

    Valid combos:
    1 + 1 + 6 = 8  ✓  (using both 1s is OK, they're separate elements)
    1 + 2 + 5 = 8  ✓
    1 + 7     = 8  ✓
    2 + 6     = 8  ✓

How to avoid duplicate combos:
  After sorting, if the same number appears again at the same depth
  of recursion, SKIP it.

    Sorted: [1, 1, 2, 5, 6, 7, 10]
                 ↑
    At depth 0, we already tried starting with 1 (index 0).
    When we reach 1 (index 1) at the same depth → SKIP!
    This prevents [1,7] from appearing twice.
"""
