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

def test_merge_two_lists():
    s = Solution()
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    merged = s.mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]
    
    assert s.mergeTwoLists(None, None) == None
