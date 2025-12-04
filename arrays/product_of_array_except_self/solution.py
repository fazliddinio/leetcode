"""
# Product of Array Except Self

## Problem Description
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

## Approaches
1.  **Brute Force**: Calculate product for each element using nested loops.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1) (ignoring output array)
2.  **Prefix and Postfix Arrays** (Alternative): Use two separate arrays to store prefix and suffix products.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
3.  **Optimal**: Calculate prefix products in the result array, then multiply by suffix products on the fly.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1) (output array does not count as extra space)
"""

from typing import List

class Solution:
    """
    Optimal Solution: O(1) Space (Two Pass)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements of `nums` except `nums[i]`.

        Args:
            nums: A list of integers.

        Returns:
            A list where the i-th element is the product of all elements of nums except nums[i].
            
        Time Complexity: O(n) - Two passes over the array.
        Space Complexity: O(1) - The output array does not count as extra space.
        """
        n = len(nums)
        result = [1] * n
        
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
            
        postfix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
            
        return result

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates product except self using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        res = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            res.append(prod)
        return res

class SolutionAlternative:
    """
    Alternative Solution: Explicit Prefix/Suffix Arrays
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates product using O(n) extra space.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
            
        return [prefix[i] * suffix[i] for i in range(n)]