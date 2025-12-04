"""
# Group Anagrams

## Problem Description
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Approaches
1.  **Count as Key** (Optimal): Use a tuple of character counts (size 26) as the key for hash map.
    *   Time Complexity: O(N * K)
    *   Space Complexity: O(N * K)
2.  **Sorted String as Key** (Alternative): Sort each string to use as key.
    *   Time Complexity: O(N * K log K)
    *   Space Complexity: O(N * K)
"""

from typing import List, DefaultDict, Tuple, Dict
from collections import defaultdict

class Solution:
    """
    Optimal Solution: Count Tuple Key
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups an array of strings into anagrams using character count as key.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists, where each inner list contains anagrams.

        Time Complexity: O(N * K) - where N is the number of strings and K is the maximum length of a string.
        Space Complexity: O(N * K) - We store all strings in the output structure.
        """
        anagram_map: DefaultDict[Tuple[int, ...], List[str]] = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())

class SolutionSorting:
    """
    Alternative Solution: Sorted String Key
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams using sorted string as key.
        
        Time Complexity: O(N * K log K)
        Space Complexity: O(N * K)
        """
        anagram_map: Dict[str, List[str]] = defaultdict(list)
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_map[sorted_s].append(s)
            
        return list(anagram_map.values())