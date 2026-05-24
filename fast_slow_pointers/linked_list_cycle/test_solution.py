import pytest
from solution import Solution, ListNode

@pytest.fixture
def solution():
    return Solution()

def _build_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    nodes = [head]
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
    if pos >= 0:
        curr.next = nodes[pos]
    return head

def test_hasCycle_example1(solution):
    head = _build_list([3, 2, 0, -4], 1)
    assert solution.hasCycle(head) is True
    assert solution.hasCycle_hash(head) is True

def test_hasCycle_example2(solution):
    head = _build_list([1, 2], 0)
    assert solution.hasCycle(head) is True
    assert solution.hasCycle_hash(head) is True

def test_hasCycle_example3(solution):
    head = _build_list([1], -1)
    assert solution.hasCycle(head) is False
    assert solution.hasCycle_hash(head) is False

def test_hasCycle_empty(solution):
    head = _build_list([], -1)
    assert solution.hasCycle(head) is False
    assert solution.hasCycle_hash(head) is False
