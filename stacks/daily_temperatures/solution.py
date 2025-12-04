"""
# Daily Temperatures

## Problem Description
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`.

## Approaches
1.  **Brute Force**: For each day, scan future days to find the first warmer temperature.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1) (excluding result)
2.  **Monotonic Stack** (Optimal): Maintain a decreasing stack of indices.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import List, Tuple

class Solution:
    """
    Optimal Solution: Monotonic Stack
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Calculates waiting days using monotonic stack.
        
        Args:
            temperatures: Daily temperatures.
            
        Returns:
            Waiting days list.
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Calculates waiting days using nested loops.
        Time Complexity: O(n^2)
        """
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res
