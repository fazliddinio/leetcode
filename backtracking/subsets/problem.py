"""
==========================================
  Subsets (LeetCode 78)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array `nums` of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution
in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10
    - All the numbers of nums are unique.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

List ALL possible groups you can make from the numbers (including the
empty group and the full group).

    nums = [1, 2, 3]

    []  [1]  [2]  [3]  [1,2]  [1,3]  [2,3]  [1,2,3]
    → 8 subsets (2^3 = 8)

For each number, you have TWO choices: include it or skip it.

    Number 1: include or skip?
    Number 2: include or skip?
    Number 3: include or skip?

Decision tree:
                    []
                 /      \
            skip 1     take 1
             []          [1]
           /    \\      /    \
        skip 2  take 2  skip 2  take 2
         []     [2]     [1]    [1,2]
        / \\   / \\    / \\    / \
       s3  t3 s3 t3  s3  t3 s3  t3
       [] [3] [2][2,3] [1][1,3] [1,2][1,2,3]

All leaves = all subsets!
"""
