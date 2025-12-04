import pytest
from .solution import Solution, SolutionSet, ListNode

def create_linked_list_cycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
    
    if pos != -1:
        current.next = nodes[pos]
    return head

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionSet])
@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ],
)
def test_has_cycle(SolutionClass, values, pos, expected):
    solution = SolutionClass()
    head = create_linked_list_cycle(values, pos)
    assert solution.hasCycle(head) == expected
