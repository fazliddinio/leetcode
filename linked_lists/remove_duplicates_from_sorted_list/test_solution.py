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
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([], []),
    ],
)
def test_delete_duplicates(SolutionClass, values, expected):
    solution = SolutionClass()
    head = create_linked_list(values)
    result = solution.deleteDuplicates(head)
    assert linked_list_to_list(result) == expected
