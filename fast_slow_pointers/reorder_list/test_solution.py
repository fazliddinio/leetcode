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

def test_reorderList_example1(solution):
    head1 = _build_list([1, 2, 3, 4])
    head2 = _build_list([1, 2, 3, 4])
    
    solution.reorderList(head1)
    solution.reorderList_array(head2)
    
    assert _to_list(head1) == [1, 4, 2, 3]
    assert _to_list(head2) == [1, 4, 2, 3]

def test_reorderList_example2(solution):
    head1 = _build_list([1, 2, 3, 4, 5])
    head2 = _build_list([1, 2, 3, 4, 5])
    
    solution.reorderList(head1)
    solution.reorderList_array(head2)
    
    assert _to_list(head1) == [1, 5, 2, 4, 3]
    assert _to_list(head2) == [1, 5, 2, 4, 3]

def test_reorderList_empty(solution):
    solution.reorderList(None)
    solution.reorderList_array(None)
    # Does not crash
    
def test_reorderList_single(solution):
    head1 = _build_list([1])
    head2 = _build_list([1])
    
    solution.reorderList(head1)
    solution.reorderList_array(head2)
    
    assert _to_list(head1) == [1]
    assert _to_list(head2) == [1]
