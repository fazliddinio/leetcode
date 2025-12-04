"""
# Happy Number

## Problem Description
Write an algorithm to determine if a number `n` is happy.
A happy number is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy.

## Approaches
1.  **Hash Set** (Brute Force/Alternative): Detect cycles using a hash set.
    *   Time Complexity: O(log n)
    *   Space Complexity: O(log n)
2.  **Fast & Slow Pointers** (Optimal): Use Floyd's Cycle-Finding Algorithm. Treat the sequence of numbers as a linked list.
    *   Time Complexity: O(log n)
    *   Space Complexity: O(1)
"""

from typing import Set

class Solution:
    """
    Optimal Solution: Fast & Slow Pointers
    """
    def isHappy(self, n: int) -> bool:
        """
        Determines if a number n is a happy number using O(1) space.
        
        Args:
            n: a positive integer
            
        Returns:
            True if n is a happy number, False otherwise.
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        slow, fast = n, self.sumOfSquares(n)
        while fast != 1 and slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            
        return fast == 1

    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n //= 10
        return output

class SolutionSet:
    """
    Alternative Solution: Hash Set
    """
    def isHappy(self, n: int) -> bool:
        """
        Determines if n is happy using Set.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n)
        """
        visit: Set[int] = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n //= 10
        return output
