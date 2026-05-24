"""
Asteroid Collision
LeetCode 735

Approach: Stack Simulation
Time: O(n) — Each asteroid pushed/popped at most once.
Space: O(n) — Stack storage.
Brute: O(n^2) — Repeatedly scan and resolve adjacent collisions until stable.
"""

from typing import List


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and (stack[-1] > 0):
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack
