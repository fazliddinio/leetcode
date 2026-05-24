"""
==========================================
  Pascal's Triangle (LeetCode 118)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer `numRows`, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it.

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    - 1 <= numRows <= 30


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Build a triangle of numbers where each number is the sum of the two
numbers above it. The edges are always 1.

        1              Row 0
       1 1             Row 1
      1 2 1            Row 2
     1 3 3 1           Row 3
    1 4 6 4 1          Row 4

How to build each row:
  - First and last element are always 1.
  - Middle elements = sum of two elements above.

    Row 3, position 1:  row2[0] + row2[1] = 1 + 2 = 3
    Row 3, position 2:  row2[1] + row2[2] = 2 + 1 = 3

         1
        1 1
       1 2 1
      1 [3] 3 1     ← 3 = 1+2 from above
     1 4 6 4 1

Algorithm:
  1. Start with [[1]].
  2. For each new row:
     - Start with 1
     - Add pairs from previous row
     - End with 1
"""
