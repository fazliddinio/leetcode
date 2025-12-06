"""
# Valid Parentheses

## Approaches
  **Stack** (Optimal): Iterate through string, pushing open brackets and popping matching closed brackets.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
