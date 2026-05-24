"""
==========================================
  Number of Islands (LeetCode 200)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Count the blobs of 1s in a grid.

Method: DFS or BFS!
  1. Loop over every cell in the grid.
  2. When you hit a '1', you found an island! Update your total count.
  3. Kick off a search (DFS/BFS) to "sink" (turn into '0' or mark visited) all connected '1's so you don't count them again!
"""
