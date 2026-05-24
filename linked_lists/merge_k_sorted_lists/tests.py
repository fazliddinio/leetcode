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
        Test merging multiple lists of varying lengths.
        Input: [[1,4,5],[1,3,4],[2,6]]
        Expected Output: [1,1,2,3,4,4,5,6]
        Explanation: All elements are merged into a single sorted list.
        """
        lists = [
            create_linked_list([1, 4, 5]),
            create_linked_list([1, 3, 4]),
            create_linked_list([2, 6])
        ]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_empty_lists(self):
        """
        Test with an empty list of lists.
        Input: []
        Expected Output: []
        Explanation: No lists provided, result is empty.
        """
        self.assertEqual(linked_list_to_list(self.solution.mergeKLists([])), [])

    def test_empty_sublist(self):
        """
        Test list of empty lists.
        Input: [[]]
        Expected Output: []
        Explanation: One empty list provided.
        """
        lists = [create_linked_list([])]
        self.assertEqual(linked_list_to_list(self.solution.mergeKLists(lists)), [])

    def test_mixed_empty_and_non_empty(self):
        """
        Test mixed empty and non-empty lists.
        Input: [[], [1], [], [2]]
        Expected Output: [1, 2]
        Explanation: Empty lists are skipped, valid ones merged.
        """
        lists = [
            create_linked_list([]),
            create_linked_list([1]),
            create_linked_list([]),
            create_linked_list([2])
        ]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_single_element_lists(self):
        """
        Test merging lists each containing a single element.
        Input: [[3], [1], [2]]
        Expected Output: [1, 2, 3]
        Explanation: Sorted order is maintained.
        """
        lists = [
            create_linked_list([3]),
            create_linked_list([1]),
            create_linked_list([2])
        ]
        result = self.solution.mergeKLists(lists)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
