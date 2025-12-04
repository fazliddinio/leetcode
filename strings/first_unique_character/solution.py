"""
# First Unique Character in a String

## Problem Description
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

## Approaches
1.  **Brute Force**: For each character, check if it duplicates in the rest of the string.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Array Constrained Map** (Alternative): Since s consists of only lowercase English letters, use an array of size 26.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
3.  **Hash Map** (Optimal): Use a hash map to count frequencies.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1) (alphabet size constant)
"""

from typing import Dict, List

class Solution:
    """
    Optimal Solution: Hash Map
    """
    def firstUniqChar(self, s: str) -> int:
        """
        Finds the first non-repeating character in a string and return its index.
        
        Args:
            s: The input string.

        Returns:
            The index of the first unique character. Returns -1 if it doesn't exist.

        Time Complexity: O(n) - We iterate through the string twice.
        Space Complexity: O(1) - Since the alphabet size is constant.
        """
        count: Dict[str, int] = {}
        
        # Build frequency map
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Find first character with frequency 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def firstUniqChar(self, s: str) -> int:
        """
        Finds first unique char using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(s)
        for i in range(n):
            unique = True
            for j in range(n):
                if i != j and s[i] == s[j]:
                    unique = False
                    break
            if unique:
                return i
        return -1

class SolutionAlternative:
    """
    Alternative Solution: Fixed Size Array
    """
    def firstUniqChar(self, s: str) -> int:
        """
        Finds first unique char using an array for frequency (assuming lowercase English).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = [0] * 26
        offset = ord('a')
        
        for char in s:
            count[ord(char) - offset] += 1
            
        for i, char in enumerate(s):
            if count[ord(char) - offset] == 1:
                return i
        return -1
