"""
# Min Stack

## Problem Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the `MinStack` class.

## Approaches
1.  **Single Stack (Scan Min)** (Brute Force/Alternative): Standard stack. For `getMin`, scan the stack.
    *   Time Complexity: O(1) for push/pop/top. O(N) for getMin.
    *   Space Complexity: O(N)
2.  **Two Stacks** (Optimal): Use an auxiliary stack to store the minimums.
    *   Time Complexity: O(1) for all operations.
    *   Space Complexity: O(N)
"""

from typing import List

class MinStack:
    """
    Optimal Solution: Two Stacks
    """
    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

class MinStackSlow:
    """
    Alternative Solution: Single Stack, O(N) getMin
    """
    def __init__(self):
        self.stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
