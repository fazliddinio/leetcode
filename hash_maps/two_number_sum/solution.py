"""
Two Sum (AlgoExpert variant)
LeetCode 1

Approach: Hash Map
Time: O(n) — Single pass.
Space: O(n) — Store seen numbers.
Brute: O(n^2) — Check all pairs with nested loops.
"""

from typing import List


class Solution:

    def twoNumberSum(self, array: List[int], targetSum: int) -> List[int]:
        seen = set()
        for num in array:
            complement = targetSum - num
            if complement in seen:
                return [complement, num]
            seen.add(num)
        return []
