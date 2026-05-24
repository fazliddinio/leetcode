"""
Fruit Into Baskets
LeetCode 904

Approach: Sliding Window + Hash Map
Time: O(n) — single pass
Space: O(1) — at most 3 elements in the hash map
Brute: O(n²) — try starting from every tree
"""

from typing import List
from collections import defaultdict


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        """Sliding Window Hash Map Approach"""
        left = 0
        max_fruits = 0
        basket = defaultdict(int)
        for right in range(len(fruits)):
            basket[fruits[right]] += 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits
