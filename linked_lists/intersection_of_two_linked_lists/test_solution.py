import pytest
from .solution import Solution, SolutionSet, ListNode

def create_intersected_list(listA_vals, listB_vals, intersect_val, skipA, skipB):
    # Constructing manually to ensure object identity for intersection
    headA = ListNode(0) # dummy
    currA = headA
    
    headB = ListNode(0) # dummy
    currB = headB
    
    intersect_node = None
    
    # Common part
    common_nodes = []
    # Logic to build list based onvals is tricky with intersection param.
    # Simplified: Build ListA, Build ListB. Link them.
    
    # Actually, simpler:
    # listA = [4,1,8,4,5], listB = [5,6,1,8,4,5] intersectVal = 8
    # 8, 4, 5 part is shared.
    pass 
    # Let's just create simple structure for test
    # A: 1 -> 2 -> 3
    # B: 4 -> 3 (same 3)
    
    node3 = ListNode(3)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node3
    
    node4 = ListNode(4)
    node4.next = node3
    
    return node1, node4, node3

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionSet])
def test_get_intersection_node(SolutionClass):
    solution = SolutionClass()
    # Simple case: 1->2->3, 4->3, intersect at 3
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    node1.next = node2
    node2.next = node3
    
    node4 = ListNode(4)
    node4.next = node3
    
    res = solution.getIntersectionNode(node1, node4)
    assert res == node3
    
    # No intersection
    n1 = ListNode(1)
    n2 = ListNode(2)
    res = solution.getIntersectionNode(n1, n2)
    assert res is None
