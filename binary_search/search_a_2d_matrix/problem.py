"""
==========================================
  Search a 2D Matrix (LeetCode 74)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given an m x n integer matrix `matrix` with the following
properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of
      the previous row.

Given an integer `target`, return `true` if target is in matrix, or
`false` otherwise.

You must write an algorithm with O(log(m * n)) runtime complexity.

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
    - m == matrix.length, n == matrix[i].length
    - 1 <= m, n <= 100
    - -10^4 <= matrix[i][j], target <= 10^4


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

The 2D matrix is really just a sorted list folded into rows.
Treat it as a flat sorted array and do binary search!

    Matrix:
    [ 1,  3,  5,  7]     → indices 0-3
    [10, 11, 16, 20]     → indices 4-7
    [23, 30, 34, 60]     → indices 8-11

    Flat: [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
    target = 3

    Index → row, col conversion:
    index 5 → row = 5 // 4 = 1,  col = 5 % 4 = 1  → matrix[1][1] = 11

    Binary search on indices 0 to 11:
    mid=5 → matrix[1][1]=11 > 3 → go left
    mid=2 → matrix[0][2]=5 > 3  → go left
    mid=1 → matrix[0][1]=3 == 3 → FOUND! ★
"""
