"""
==========================================
  Permutations (LeetCode 46)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an array `nums` of distinct integers, return all the possible
permutations. You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
    - 1 <= nums.length <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Arrange all numbers in EVERY possible order.

    nums = [1, 2, 3]

    123, 132, 213, 231, 312, 321  →  6 arrangements (3! = 6)

Think of it as filling slots:

    Slot 1: pick any of [1, 2, 3]
    Slot 2: pick from remaining
    Slot 3: whatever's left

    Pick 1 first:  1 _ _  →  1 2 3  or  1 3 2
    Pick 2 first:  2 _ _  →  2 1 3  or  2 3 1
    Pick 3 first:  3 _ _  →  3 1 2  or  3 2 1

Decision tree:
              [1,2,3]
           /     |     \
         1       2       3
        / \\    / \\    / \
       2   3  1   3  1   2
       |   |  |   |  |   |
       3   2  3   1  2   1
    [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
"""
