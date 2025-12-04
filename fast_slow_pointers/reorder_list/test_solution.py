import pytest
from .solution import Solution, SolutionArray, ListNode

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

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionArray])
@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),
    ],
)
def test_reorder_list(SolutionClass, values, expected):
    solution = SolutionClass()
    head = create_linked_list(values)
    solution.reorderList(head)
    assert linked_list_to_list(head) == expected
