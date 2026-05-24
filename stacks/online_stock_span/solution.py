"""
Online Stock Span
LeetCode 901

Approach: Monotonic Stack
Time: O(1) Amortized — Each element pushed/popped once.
Space: O(n) — Stack storage.
Brute: O(n) — For each call, scan backwards through all previous prices.
"""


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
