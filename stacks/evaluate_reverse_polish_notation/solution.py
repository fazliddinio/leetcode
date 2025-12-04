"""
# Evaluate Reverse Polish Notation

## Problem Description
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.

## Approaches
1.  **Global Stack** (Optimal): Iterate through tokens, push numbers, pop and compute for operators.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
2.  **Recursive** (Alternative): Recursive evaluation (works well if we process from end to start for Prefix, but for Postfix we can simulate stack with recursion or modify list).
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Stack
    """
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates RPN using stack.
        
        Args:
            tokens: A list of strings representing the expression.
            
        Returns:
            The value of the expression.
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack: List[int] = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

class SolutionRecursive:
    """
    Alternative Solution: Recursive (using list as stack implicitly)
    """
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates by processing tokens from end (which effectively reverses it to Prefix-like structure logic or we assume we pop from end).
        Wait, RPN: 2 1 + 3 * -> (2+1)*3.
        Last element is the root operator *.
        So if we pop from end:
        * -> Op1 (Recurse) -> Op2 (Recurse).
        Op2 is 3. Op1 is +.
        + -> Op1 (1), Op2 (2).
        Yes, processing from right to left makes it recursive.
        """
        token = tokens.pop()
        if token not in "+-*/":
            return int(token)
        
        # Right operand is at the top of stack (end of list)
        right = self.evalRPN(tokens)
        left = self.evalRPN(tokens)
        
        if token == "+":
            return left + right
        elif token == "-":
            return left - right
        elif token == "*":
            return left * right
        elif token == "/":
            return int(left / right)
        return 0
