import pytest
from .solution import Solution, ListNode

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def test_is_palindrome():
    s = Solution()
    assert s.isPalindrome(create_linked_list([1, 2, 2, 1])) == True
    assert s.isPalindrome(create_linked_list([1, 2])) == False
