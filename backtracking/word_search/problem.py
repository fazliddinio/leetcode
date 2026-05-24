"""
==========================================
  Word Search (LeetCode 79)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an m x n grid of characters `board` and a string `word`, return
`true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example 1:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:
    Input: board = [["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"]], word = "ABCB"
    Output: false

Constraints:
    - m == board.length, n = board[i].length
    - 1 <= m, n <= 6
    - 1 <= word.length <= 15
    - board and word consists of only lowercase and uppercase English letters.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Can you trace out a word on the grid by moving up/down/left/right?
Each cell can only be used once per word.

    Board:                Find "ABCCED":
    A  B  C  E
    S  F  C  S            A → B → C → C → E → D  ✓
    A  D  E  E                        ↓
                                  (goes down to row 2)

    Path on the board:
    [A] [B] [C]  E        A(0,0) → B(0,1) → C(0,2)
     S   F  [C]  S                             ↓
     A  [D] [E]  E                          C(1,2) → E(2,2) → D(2,1)

How it works:
  1. Find the first letter of the word on the board.
  2. From there, try moving in 4 directions for the next letter.
  3. Mark visited cells so we don't reuse them.
  4. If we match all letters → True!
  5. If stuck → backtrack (unmark) and try another direction.

It's like solving a maze where you need to spell a word!
"""
