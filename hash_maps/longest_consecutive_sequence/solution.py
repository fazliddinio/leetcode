"""
# Longest Consecutive Sequence

## Problem Description
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

## Approaches
1.  **Brute Force**: For each number, attempt to count the streak by searching for `num+1` in the array.
    *   Time Complexity: O(n^3) if checking "in list", or O(n^2) if using brute force search.
    *   Space Complexity: O(1)
2.  **Sorting** (Alternative): Sort the array and scan for streaks.
    *   Time Complexity: O(n log n)
    *   Space Complexity: O(1) or O(n)
3.  **Hash Set** (Optimal): Use a Set to allow O(1) lookups. Only iterate when at start of sequence.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Hash Set
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence.
        
        Args:
            nums: A list of integers.
            
        Returns:
            The length of the longest consecutive elements sequence.
            
        Time Complexity: O(n) - We iterate through the array and set lookups are O(1).
        Space Complexity: O(n) - We use a set to store array elements.
        """
        num_set = set(nums)
        longest = 0
        
        for n in nums:
            # Check if it's the start of a sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
                
        return longest

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds longest streak using brute force.
        
        Time Complexity: O(n^2) (average if 'in' is fast? No, 'in list' is O(n), so O(n^3) worst case, O(n^2) if optimized logic)
        Actually: Outer loop n, inner while loop checks n+1 in list (O(n)). So O(n^2) * streak_len.
        """
        longest = 0
        for num in nums:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
        return longest if nums else 0

class SolutionSorting:
    """
    Alternative Solution: Sorting
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds streak by sorting.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1) or O(n)
        """
        if not nums:
            return 0
            
        nums.sort()
        
        longest = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                else:
                    longest = max(longest, current_streak)
                    current_streak = 1
        return max(longest, current_streak)