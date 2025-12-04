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
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_add_two_numbers(SolutionClass, l1, l2, expected):
    solution = SolutionClass()
    h1 = create_linked_list(l1)
    h2 = create_linked_list(l2)
    # Recursion with default arg mismatch? No, Python handles kwargs or positional. 
    # But SolutionRecursive signature has carry. Solution does not.
    # SolutionRecursive.addTwoNumbers(l1, l2) matches.
    result = solution.addTwoNumbers(h1, h2)
    assert linked_list_to_list(result) == expected
