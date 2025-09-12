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

def test_remove_nth_from_end():
    s = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    new_head = s.removeNthFromEnd(head, 2)
    assert linked_list_to_list(new_head) == [1, 2, 3, 5]
    
    head = create_linked_list([1])
    new_head = s.removeNthFromEnd(head, 1)
    assert linked_list_to_list(new_head) == []
