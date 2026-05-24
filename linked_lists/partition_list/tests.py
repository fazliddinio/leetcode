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
        Test typical partition.
        Input: head = [1,4,3,2,5,2], x = 3
        Expected Output: [1,2,2,4,3,5]
        Explanation: 
        Elements < 3: 1, 2, 2
        Elements >= 3: 4, 3, 5
        Combined: [1, 2, 2, 4, 3, 5]
        """
        head = create_linked_list([1, 4, 3, 2, 5, 2])
        result = self.solution.partition(head, 3)
        self.assertEqual(linked_list_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_example_2(self):
        """
        Test existing sorted small list.
        Input: head = [2,1], x = 2
        Expected Output: [1,2]
        Explanation: 
        1 < 2, 2 >= 2.
        """
        head = create_linked_list([2, 1])
        result = self.solution.partition(head, 2)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_all_smaller(self):
        """
        Test all elements smaller than x.
        Input: head = [1, 2], x = 3
        Expected Output: [1, 2]
        """
        head = create_linked_list([1, 2])
        result = self.solution.partition(head, 3)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_all_greater_or_equal(self):
        """
        Test all elements greater or equal to x.
        Input: head = [3, 4], x = 2
        Expected Output: [3, 4]
        """
        head = create_linked_list([3, 4])
        result = self.solution.partition(head, 2)
        self.assertEqual(linked_list_to_list(result), [3, 4])

    def test_empty_list(self):
        """
        Test empty list.
        Input: head = [], x = 0
        Expected Output: []
        """
        head = create_linked_list([])
        result = self.solution.partition(head, 0)
        self.assertEqual(linked_list_to_list(result), [])

if __name__ == '__main__':
    unittest.main()
