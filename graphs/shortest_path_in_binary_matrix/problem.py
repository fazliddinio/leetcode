"""
==========================================
  Shortest Path in Binary Matrix (LeetCode 1091)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an n x n binary matrix grid, return the length of the shortest clear path
in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    - All the visited cells of the path are 0.
    - All the adjacent cells of the path are 8-directionally connected (i.e.,
      they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 2

Example 2:
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

Example 3:
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1

Constraints:
    - n == grid.length
    - n == grid[i].length
    - 1 <= n <= 100
    - grid[i][j] is 0 or 1


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Find the shortest path from top-left to bottom-right in a grid.
You can move in 8 directions (including diagonals).
Cells with 0 are passable, cells with 1 are walls.

    Grid:        Path (length 4):
    [0, 0, 0]       [*, 0, 0]
    [1, 1, 0]       [1, 1, *]
    [1, 1, 0]       [1, 1, *]
                         ↓ wait, let me trace:
    (0,0) → (0,1) → (1,2) → (2,2) = 4 steps

BFS guarantees the shortest path in an unweighted grid.
Start at (0,0), explore all 8 neighbors level by level.
First time you reach (n-1, n-1) = answer.
"""
