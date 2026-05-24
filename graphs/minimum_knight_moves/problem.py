"""
==========================================
  Minimum Knight Moves (LeetCode 1197)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

In an infinite chess board with coordinates from -infinity to +infinity,
you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is
two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].
It is guaranteed the answer exists.

Example 1:
    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] → [2, 1]

Example 2:
    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

Constraints:
    - -300 <= x <= 300
    - -300 <= y <= 300
    - 0 <= |x| + |y| <= 300


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

A chess knight starts at (0,0) on an infinite board. Find the minimum number
of L-shaped jumps to reach (x, y).

    Knight moves (like chess):
        Can jump to 8 positions from any square:
        (+2,+1), (+2,-1), (-2,+1), (-2,-1)
        (+1,+2), (+1,-2), (-1,+2), (-1,-2)

    Example: reach (2,1) from (0,0)
        One jump: (0,0) → (2,1) ✓  Answer = 1

BFS from (0,0) exploring all 8 knight moves level by level.
Due to symmetry, we can work in the first quadrant (|x|, |y|) to reduce search space.
"""
