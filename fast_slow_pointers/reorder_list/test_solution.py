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

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def test_reorder_list():
    s = Solution()
    head = create_linked_list([1, 2, 3, 4])
    s.reorderList(head)
    assert linked_list_to_list(head) == [1, 4, 2, 3]
    
    head = create_linked_list([1, 2, 3, 4, 5])
    s.reorderList(head)
    assert linked_list_to_list(head) == [1, 5, 2, 4, 3]
