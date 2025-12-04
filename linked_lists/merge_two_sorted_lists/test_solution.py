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
    "l1, l2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_merge_two_lists(SolutionClass, l1, l2, expected):
    solution = SolutionClass()
    h1 = create_linked_list(l1)
    h2 = create_linked_list(l2)
    merged = solution.mergeTwoLists(h1, h2)
    assert linked_list_to_list(merged) == expected
