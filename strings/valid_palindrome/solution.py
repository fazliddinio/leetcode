"""
# Valid Palindrome

## Problem Description
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Approaches
1.  **Reverse String** (Alternative): Clean the string and compare it with its reverse.
    *   Time Complexity: O(N)
    *   Space Complexity: O(N)
2.  **Two Pointers** (Optimal): Use two pointers starting from both ends, skipping non-alphanumeric characters.
    *   Time Complexity: O(N)
    *   Space Complexity: O(1)
"""

import re

class Solution:
    """
    Optimal Solution: Two Pointers
    """
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a palindrome using two pointers (O(1) space).

        Args:
            s: The input string.

        Returns:
            True if the string is a palindrome, False otherwise.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.is_alphanum(s[l]):
                l += 1
            while r > l and not self.is_alphanum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def is_alphanum(self, c: str) -> bool:
        return ('a' <= c.lower() <= 'z') or ('0' <= c <= '9')

class SolutionReverse:
    """
    Alternative Solution: Filtering and Reversing
    """
    def isPalindrome(self, s: str) -> bool:
        """
        Check palindrome by reversing.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned_text == cleaned_text[::-1]