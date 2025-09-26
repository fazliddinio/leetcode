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

def test_get_intersection_node():
    s = Solution()
    # Create intersecting lists
    # A: 4 -> 1 \
    #            -> 8 -> 4 -> 5
    # B: 5 -> 6 /
    intersect = create_linked_list([8, 4, 5])
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersect
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = intersect
    
    assert s.getIntersectionNode(headA, headB) == intersect
    assert s.getIntersectionNode(create_linked_list([1, 2]), create_linked_list([3, 4])) == None
