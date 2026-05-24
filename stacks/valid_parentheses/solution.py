"""
Valid Parentheses
LeetCode 20

Approach: Stack
Time: O(n) — Single pass.
Space: O(n) — Stack storage in worst case.
Brute: O(n^2) — Repeatedly strip innermost matched pairs until empty or stuck.
"""


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
