"""
Circular Array Loop
LeetCode 457

Approach: Fast and Slow Pointers
Time: O(n) — each element visited a constant number of times
Space: O(1) — marks visited elements in-place with 0
Brute: O(n) — DFS with visited array using O(n) space
"""

from typing import List


class Solution:

    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = next_index(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
                slow = next_index(slow)
                fast = next_index(next_index(fast))

            slow = i
            val = nums[i]
            while nums[slow] * val > 0:
                nxt = next_index(slow)
                nums[slow] = 0
                slow = nxt

        return False
