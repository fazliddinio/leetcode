# LeetCode Solutions

A collection of clean, optimized Python solutions for LeetCode problems, organized by pattern.

## Categories

- [Arrays](arrays/)
- [Backtracking](backtracking/)
- [Binary Search](binary_search/)
- [Bit Manipulation](bit_manipulation/)
- [Dynamic Programming](dynamic_programming/)
- [Fast & Slow Pointers](fast_slow_pointers/)
- [Graphs](graphs/)
- [Hash Maps](hash_maps/)
- [Heaps](heaps/)
- [Intervals](intervals/)
- [Linked Lists](linked_lists/)
- [Sliding Window](sliding_window/)
- [Stacks](stacks/)
- [Strings](strings/)
- [Trees](trees/)
- [Tries](tries/)
- [Two Pointers](two_pointers/)

## Solution Format

Each solution is structured for readability and interview preparation:

```python
"""
Two Sum
LeetCode 1

Approach: Hash Map
Time: O(n) — Single pass through the array.
Space: O(n) — In the worst case, we store n elements.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
```

## Goals

- **Clean Code**: Solutions are written in a human-readable, "interview-ready" style.
- **Optimal Complexity**: Focus on the most efficient approach in terms of Big O.
- **Minimal Boilerplate**: No unnecessary comments or alternative suboptimal solutions.
