"""
==========================================
  Combination Sum (LeetCode 39)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an array of distinct integers `candidates` and a target integer
`target`, return a list of all unique combinations of `candidates` where
the chosen numbers sum to `target`. You may return the combinations in
any order.

The same number may be chosen from `candidates` an unlimited number of
times. Two combinations are unique if the frequency of at least one of
the chosen numbers is different.

The test cases are generated such that the number of unique combinations
that sum up to target is less than 150 combinations for the given input.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Constraints:
    - 1 <= candidates.length <= 30
    - 2 <= candidates[i] <= 40
    - All elements of candidates are distinct.
    - 1 <= target <= 40


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Given a set of coin denominations, find ALL ways to make exact change.
You can use each coin as many times as you want.

    Coins: [2, 3, 6, 7]    Target: 7

    Way 1: 2 + 2 + 3 = 7  ✓
    Way 2: 7 = 7           ✓

    Answer: [[2,2,3], [7]]

Think of it as a tree of choices:

                    target = 7
                   /    |    \\    \
             pick 2   pick 3  pick 6  pick 7
             rem=5    rem=4   rem=1   rem=0 ✓
            / | \\      / \\       ✗
         +2  +3  +6  +2  +3
        r=3  r=2  ✗  r=2  r=1
        / \\    |       |    ✗
      +2 +3  +2      +2
      r=1 r=0✓ r=0✓   r=0✓

    Collect all paths that reach 0: [2,2,3] and [7]

Key: To avoid duplicates like [2,3,2] and [3,2,2], only pick candidates
at or after the current index (don't go backwards).
"""
