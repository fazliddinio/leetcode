import pytest
from .solution import MinStack, MinStackSlow

@pytest.mark.parametrize("StackClass", [MinStack, MinStackSlow])
def test_min_stack(StackClass):
    min_stack = StackClass()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
