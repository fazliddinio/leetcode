import pytest
from .solution import Solution, SolutionRecursive, ListNode

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

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionRecursive])
@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_reverse_list(SolutionClass, values, expected):
    solution = SolutionClass()
    head = create_linked_list(values)
    reversed_head = solution.reverseList(head)
    assert linked_list_to_list(reversed_head) == expected
