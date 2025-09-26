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

def test_add_two_numbers():
    s = Solution()
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    res = s.addTwoNumbers(l1, l2)
    assert linked_list_to_list(res) == [7, 0, 8]
    
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    res = s.addTwoNumbers(l1, l2)
    assert linked_list_to_list(res) == [0]
