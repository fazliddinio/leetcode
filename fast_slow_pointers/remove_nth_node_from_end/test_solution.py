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

def _to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def test_removeNthFromEnd_example1(solution):
    head1 = _build_list([1, 2, 3, 4, 5])
    head2 = _build_list([1, 2, 3, 4, 5])
    n = 2
    assert _to_list(solution.removeNthFromEnd(head1, n)) == [1, 2, 3, 5]
    assert _to_list(solution.removeNthFromEnd_count(head2, n)) == [1, 2, 3, 5]

def test_removeNthFromEnd_example2(solution):
    head1 = _build_list([1])
    head2 = _build_list([1])
    n = 1
    assert _to_list(solution.removeNthFromEnd(head1, n)) == []
    assert _to_list(solution.removeNthFromEnd_count(head2, n)) == []

def test_removeNthFromEnd_example3(solution):
    head1 = _build_list([1, 2])
    head2 = _build_list([1, 2])
    n = 1
    assert _to_list(solution.removeNthFromEnd(head1, n)) == [1]
    assert _to_list(solution.removeNthFromEnd_count(head2, n)) == [1]

def test_removeNthFromEnd_remove_head(solution):
    head1 = _build_list([1, 2])
    head2 = _build_list([1, 2])
    n = 2
    assert _to_list(solution.removeNthFromEnd(head1, n)) == [2]
    assert _to_list(solution.removeNthFromEnd_count(head2, n)) == [2]
