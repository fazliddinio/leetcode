"""
# Valid Parentheses

## Problem Description
Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

## Approaches
1.  **Replace String** (Brute Force): Repeatedly replace "()", "[]", "{}" with empty string.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(n) (String copies)
2.  **Stack** (Optimal): Iterate through string, pushing open brackets and popping matching closed brackets.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import Dict, List

class Solution:
    """
    Optimal Solution: Stack
    """
    def isValid(self, s: str) -> bool:
        """
        Determines if parentheses are valid using stack.
        
        Args:
            s: Input string.
            
        Returns:
            True if valid, False otherwise.
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack: List[str] = []
        close_to_open: Dict[str, str] = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

class SolutionReplace:
    """
    Alternative Solution: String Replacement
    """
    def isValid(self, s: str) -> bool:
        """
        Determines validity by replacement.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n) (immutability of strings)
        """
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return not s
