import pytest
from solution import Solution, ListNode

@pytest.fixture
def solution():
    return Solution()

def _build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def test_isPalindrome_example1(solution):
    head1 = _build_list([1, 2, 2, 1])
    head2 = _build_list([1, 2, 2, 1])
    assert solution.isPalindrome(head1) is True
    assert solution.isPalindrome_array(head2) is True

def test_isPalindrome_example2(solution):
    head1 = _build_list([1, 2])
    head2 = _build_list([1, 2])
    assert solution.isPalindrome(head1) is False
    assert solution.isPalindrome_array(head2) is False

def test_isPalindrome_odd(solution):
    head1 = _build_list([1, 2, 3, 2, 1])
    head2 = _build_list([1, 2, 3, 2, 1])
    assert solution.isPalindrome(head1) is True
    assert solution.isPalindrome_array(head2) is True
    
def test_isPalindrome_single(solution):
    head1 = _build_list([1])
    head2 = _build_list([1])
    assert solution.isPalindrome(head1) is True
    assert solution.isPalindrome_array(head2) is True
