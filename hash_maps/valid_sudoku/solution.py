"""
# Valid Sudoku

## Problem Description
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

## Approaches
1.  **Multi-Pass** (Brute Force/Alternative): Validate rows, then columns, then boxes in separate passes.
    *   Time Complexity: O(1) (Fixed board size, effectively 3 * N^2)
    *   Space Complexity: O(1)
2.  **One-Pass** (Optimal): Validate everything in a single iteration over cells.
    *   Time Complexity: O(1) (Fixed board size, N^2)
    *   Space Complexity: O(1)
"""

from typing import List
from collections import defaultdict

class Solution:
    """
    Optimal Solution: One Pass
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid in one pass.
        
        Args:
            board: A 9x9 list of lists containing strings digits '1'-'9' or '.'.
        
        Returns:
            True if the board is valid, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                    
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]):
                    return False
                    
                cols[c].add(val)
                rows[r].add(val)
                squares[(r // 3, c // 3)].add(val)
        return True

class SolutionMultiPass:
    """
    Alternative Solution: Separate Checks
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check valid sudoku with separate passes.
        """
        # Check rows
        for r in range(9):
            row_set = set()
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                if val in row_set: return False
                row_set.add(val)
                
        # Check cols
        for c in range(9):
            col_set = set()
            for r in range(9):
                val = board[r][c]
                if val == ".": continue
                if val in col_set: return False
                col_set.add(val)
                
        # Check boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[br + i][bc + j]
                        if val == ".": continue
                        if val in box_set: return False
                        box_set.add(val)
        return True
