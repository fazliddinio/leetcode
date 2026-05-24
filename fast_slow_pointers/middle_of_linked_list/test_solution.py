import pytest
from solution import Solution, ListNode

@pytest.fixture
def solution():
    return Solution()

def _build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def test_middleNode_example1(solution):
    head = _build_list([1, 2, 3, 4, 5])
    assert solution.middleNode(head).val == 3
    assert solution.middleNode_count(head).val == 3

def test_middleNode_example2(solution):
    head = _build_list([1, 2, 3, 4, 5, 6])
    assert solution.middleNode(head).val == 4
    assert solution.middleNode_count(head).val == 4
    
def test_middleNode_single(solution):
    head = _build_list([1])
    assert solution.middleNode(head).val == 1
    assert solution.middleNode_count(head).val == 1
    
def test_middleNode_two(solution):
    head = _build_list([1, 2])
    assert solution.middleNode(head).val == 2
    assert solution.middleNode_count(head).val == 2
