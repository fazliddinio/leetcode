"""
==========================================
  Combinations (LeetCode 77)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given two integers `n` and `k`, return all possible combinations of `k`
numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
    Input: n = 1, k = 1
    Output: [[1]]

Constraints:
    - 1 <= n <= 20
    - 1 <= k <= n


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Pick k numbers from 1 to n. List ALL possible groups (order doesn't matter).

    n = 4, k = 2  →  Pick 2 numbers from {1, 2, 3, 4}

    [1,2]  [1,3]  [1,4]
    [2,3]  [2,4]
    [3,4]

    (Note: [2,1] is the same as [1,2], so we only list it once)

Think of it as a decision tree:

    Start with 1? → then pick from {2,3,4}  → [1,2] [1,3] [1,4]
    Start with 2? → then pick from {3,4}    → [2,3] [2,4]
    Start with 3? → then pick from {4}      → [3,4]
    Start with 4? → nobody left to pair with!

Key insight: always pick numbers in increasing order to avoid duplicates.
"""
