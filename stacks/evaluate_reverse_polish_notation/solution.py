"""
Evaluate Reverse Polish Notation
LeetCode 150

Approach: Stack Evaluation
Time: O(n) — Single pass.
Space: O(n) — Stack storage.
Brute: O(n^2) — Repeatedly find first operator in list, compute, and splice result back.
"""

from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: int(a / b)}
        for token in tokens:
            if token in operators:
                b, a = (stack.pop(), stack.pop())
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]
