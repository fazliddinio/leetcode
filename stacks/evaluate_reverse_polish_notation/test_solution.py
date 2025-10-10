import pytest
from .solution import Solution

def test_eval_rpn():
    s = Solution()
    assert s.evalRPN(["2","1","+","3","*"]) == 9
    assert s.evalRPN(["4","13","5","/","+"]) == 6
    assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
