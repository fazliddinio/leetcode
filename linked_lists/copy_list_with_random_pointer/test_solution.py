import pytest
from .solution import Solution, Node

def test_copy_random_list():
    s = Solution()
    # Create list: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1
    
    cloned = s.copyRandomList(n1)
    
    assert cloned.val == 7
    assert cloned.next.val == 13
    assert cloned.next.random.val == 7
    
    # Verify deep copy
    assert cloned is not n1
    assert cloned.next is not n2
