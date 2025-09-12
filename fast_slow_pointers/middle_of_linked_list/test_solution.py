import pytest
from .solution import Solution, ListNode

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def test_middle_node():
    s = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    mid = s.middleNode(head)
    assert mid.val == 3
    
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    mid = s.middleNode(head)
    assert mid.val == 4
