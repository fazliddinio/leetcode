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
        Test reversing nodes in groups of 2.
        Input: head = [1,2,3,4,5], k = 2
        Expected Output: [2,1,4,3,5]
        Explanation: 
        [1,2] -> [2,1]
        [3,4] -> [4,3]
        [5] remains as is.
        """
        head = create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseKGroup(head, 2)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3, 5])

    def test_example_2(self):
        """
        Test reversing nodes in groups of 3.
        Input: head = [1,2,3,4,5], k = 3
        Expected Output: [3,2,1,4,5]
        Explanation: 
        [1,2,3] -> [3,2,1]
        [4,5] remains as is because length < k.
        """
        head = create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseKGroup(head, 3)
        self.assertEqual(linked_list_to_list(result), [3, 2, 1, 4, 5])

    def test_k_is_one(self):
        """
        Test with k = 1.
        Input: head = [1,2,3], k = 1
        Expected Output: [1,2,3]
        Explanation: Groups of 1 mean no change in order.
        """
        head = create_linked_list([1, 2, 3])
        result = self.solution.reverseKGroup(head, 1)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_single_element(self):
        """
        Test with a single element list.
        Input: head = [1], k = 1
        Expected Output: [1]
        """
        head = create_linked_list([1])
        result = self.solution.reverseKGroup(head, 1)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_list_shorter_than_k(self):
        """
        Test when list length is less than k.
        Input: head = [1, 2], k = 3
        Expected Output: [1, 2]
        Explanation: No reversal should happen.
        """
        head = create_linked_list([1, 2])
        result = self.solution.reverseKGroup(head, 3)
        self.assertEqual(linked_list_to_list(result), [1, 2])

if __name__ == '__main__':
    unittest.main()
