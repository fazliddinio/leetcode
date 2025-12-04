import pytest
from .solution import Solution, SolutionArray, ListNode

def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionArray])
@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([], True), # Or False? Usually empty is palindrome of empty string logic. Code handles it? fast=None, slow=None. loop doesn't run. prev=None. right=None. Returns True.
    ],
)
def test_is_palindrome(SolutionClass, values, expected):
    solution = SolutionClass()
    head = create_linked_list(values)
    assert solution.isPalindrome(head) == expected
