import pytest
from solution import Solution, ListNode

@pytest.fixture
def solution():
    return Solution()

def _build_list(values, pos):
    if not values:
        return None, None
    head = ListNode(values[0])
    curr = head
    nodes = [head]
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
    if pos >= 0:
        curr.next = nodes[pos]
    return head, (nodes[pos] if pos >= 0 else None)

def test_detectCycle_example1(solution):
    head, expected = _build_list([3, 2, 0, -4], 1)
    assert solution.detectCycle(head) == expected
    assert solution.detectCycle_hash(head) == expected

def test_detectCycle_example2(solution):
    head, expected = _build_list([1, 2], 0)
    assert solution.detectCycle(head) == expected
    assert solution.detectCycle_hash(head) == expected

def test_detectCycle_no_cycle(solution):
    head, expected = _build_list([1], -1)
    assert solution.detectCycle(head) == expected
    assert solution.detectCycle_hash(head) == expected

def test_detectCycle_empty(solution):
    head, expected = _build_list([], -1)
    assert solution.detectCycle(head) == expected
    assert solution.detectCycle_hash(head) == expected
