import pytest
from .solution import Solution, SolutionCount, ListNode

def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionCount])
@pytest.mark.parametrize(
    "values, expected_values",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
        ([1], [1]),
    ],
)
def test_middle_node(SolutionClass, values, expected_values):
    solution = SolutionClass()
    head = create_linked_list(values)
    mid = solution.middleNode(head)
    assert linked_list_to_list(mid) == expected_values
