import pytest
from .solution import Solution, Node

def test_clone_graph():
    s = Solution()
    # Adj List: [[2,4],[1,3],[2,4],[1,3]]
    # Node 1 -> 2, 4
    # Node 2 -> 1, 3
    # Node 3 -> 2, 4
    # Node 4 -> 1, 3
    
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    
    cloned = s.cloneGraph(n1)
    
    assert cloned.val == 1
    assert cloned is not n1
    assert len(cloned.neighbors) == 2
    # Verify connectivity conceptually (simple check)
    vals = sorted([n.val for n in cloned.neighbors])
    assert vals == [2, 4]
