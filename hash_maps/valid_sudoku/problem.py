"""
==========================================
  Valid Sudoku (LeetCode 36)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be validated.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Check if the current state of a Sudoku board follows the basic rules! We don't need to solve it.

Method: Use 3 sets (or arrays) to track seen digits.
  - Track seen numbers per row: `seen_rows[row]`
  - Track seen numbers per col: `seen_cols[col]`
  - Track seen numbers per 3x3 box: `seen_boxes[row // 3][col // 3]`

  Iterate over each cell. If it's empty (`.`), skip it. If a digit is already in the row, column, or 3x3 box set, return False!
"""
