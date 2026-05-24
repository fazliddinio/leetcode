"""
Remove All Adjacent Duplicates In String
LeetCode 1047

Approach: Stack
Time: O(n) — Single pass.
Space: O(n) — Stack/Output storage.
Brute: O(n^2) — Repeatedly scan and remove adjacent duplicate pairs until stable.
"""


class Solution:

    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
