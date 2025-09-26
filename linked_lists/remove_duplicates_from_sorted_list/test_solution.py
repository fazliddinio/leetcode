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

def test_delete_duplicates():
    s = Solution()
    head = create_linked_list([1, 1, 2])
    new_head = s.deleteDuplicates(head)
    assert linked_list_to_list(new_head) == [1, 2]
    
    head = create_linked_list([1, 1, 2, 3, 3])
    new_head = s.deleteDuplicates(head)
    assert linked_list_to_list(new_head) == [1, 2, 3]
