# LeetCode 150: Evaluate Reverse Polish Notation
# Time: O(n), Space: O(n)

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in '+-*/':
                b, a = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        
        return stack[0]
