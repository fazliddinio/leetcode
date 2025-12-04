import pytest
from .solution import Solution, SolutionTwoPass, ListNode

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

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionTwoPass])
@pytest.mark.parametrize(
    "values, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ],
)
def test_remove_nth_from_end(SolutionClass, values, n, expected):
    solution = SolutionClass()
    head = create_linked_list(values)
    result_head = solution.removeNthFromEnd(head, n)
    assert linked_list_to_list(result_head) == expected
