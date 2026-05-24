import unittest
from solution import Solution, ListNode

# Helper to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Test typical odd/even grouping.
        Input: [1, 2, 3, 4, 5]
        Expected Output: [1, 3, 5, 2, 4]
        Explanation: 
        Odds: 1, 3, 5
        Evens: 2, 4
        """
        head = create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1, 3, 5, 2, 4])

    def test_example_2(self):
        """
        Test longer list.
        Input: [2, 1, 3, 5, 6, 4, 7]
        Expected Output: [2, 3, 6, 7, 1, 5, 4]
        Explanation: 
        Odds (by index): 2, 3, 6, 7
        Evens (by index): 1, 5, 4
        """
        head = create_linked_list([2, 1, 3, 5, 6, 4, 7])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [2, 3, 6, 7, 1, 5, 4])

    def test_empty_list(self):
        """
        Test empty list.
        Input: []
        Expected Output: []
        """
        head = create_linked_list([])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_single_element(self):
        """
        Test single element list.
        Input: [1]
        Expected Output: [1]
        """
        head = create_linked_list([1])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_two_elements(self):
        """
        Test two elements (already sorted by odd/even indices).
        Input: [1, 2]
        Expected Output: [1, 2]
        """
        head = create_linked_list([1, 2])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1, 2])

if __name__ == '__main__':
    unittest.main()
