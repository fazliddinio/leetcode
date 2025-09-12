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

def test_has_cycle():
    s = Solution()
    # Create cycle: 3 -> 2 -> 0 -> -4 -> 2
    head = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node4 = ListNode(-4)
    head.next = node2
    node2.next = node0
    node0.next = node4
    node4.next = node2
    
    assert s.hasCycle(head) == True
    assert s.hasCycle(create_linked_list([1, 2])) == False
    assert s.hasCycle(None) == False
