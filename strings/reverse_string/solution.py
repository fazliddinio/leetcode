"""
# Reverse String

## Problem Description
Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place with O(1) extra memory.

## Approaches
1.  **Two Pointers** (Optimal): Swap characters from start and end moving towards center.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
2.  **Recursion** (Alternative): Recursive swapping. Note: Uses O(n) stack space, violating O(1) constraint effectively, but demonstrates recursion.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n) due to recursion stack.
3.  **Built-in** (Pythonic): `s.reverse()`.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Two Pointers
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses a string (given as a list of characters) in-place.

        Args:
            s: The list of characters to reverse.

        Returns:
            None. Modifies s in-place.

        Time Complexity: O(n) - We iterate through half of the list.
        Space Complexity: O(1) - We use constant extra space.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

class SolutionRecursive:
    """
    Alternative Solution: Recursion
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses using recursion.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def helper(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)
            
        helper(0, len(s) - 1)

class SolutionBuiltIn:
    """
    Alternative Solution: Built-in
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses using built-in method.
        """
        s.reverse()