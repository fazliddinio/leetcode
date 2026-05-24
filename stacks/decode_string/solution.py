"""
Decode String
LeetCode 394

Approach: Stack
Time: O(L) — L is length of decoded string.
Space: O(L) — Stack/Recursion depth + Output.
Brute: O(L^2) — Repeatedly find and expand innermost brackets each pass.
"""


class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ''
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ''
                current_num = 0
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char
        return current_string
