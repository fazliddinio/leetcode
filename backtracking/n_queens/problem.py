"""
==========================================
  N-Queens (LeetCode 51)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

The n-queens puzzle is the problem of placing n queens on an n × n
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.

Example 1:
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],
             ["..Q.","Q...","...Q",".Q.."]]

Example 2:
    Input: n = 1
    Output: [["Q"]]

Constraints:
    - 1 <= n <= 9


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Place N queens on an N×N board so NONE can attack each other.
Queens attack in rows, columns, and both diagonals.

    For n=4, two solutions exist:

    Solution 1:          Solution 2:
    . Q . .              . . Q .
    . . . Q              Q . . .
    Q . . .              . . . Q
    . . Q .              . Q . .

    A queen (Q) attacks ←→ ↑↓ and diagonally ↗↘↙↖

Strategy: Place queens ONE ROW at a time.
    Row 0: try each column
    Row 1: try each column (skip if attacked)
    Row 2: try each column (skip if attacked)
    ...

    Three things to check before placing:
    1. No queen in same COLUMN
    2. No queen on same DIAGONAL (row-col = constant)
    3. No queen on same ANTI-DIAGONAL (row+col = constant)

    . Q . .   ← place Q at (0,1)
    . . . Q   ← (1,0)✗col (1,1)✗diag (1,2)✗diag (1,3)✓
    Q . . .   ← (2,0)✓
    . . Q .   ← (3,2)✓  → Valid solution!
"""
