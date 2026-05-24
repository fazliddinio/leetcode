import unittest
from collections import deque
from solution import Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Test with a standard binary tree structure.
        Input: [1, 2, 3, null, 5, null, 4]
        Expected Output: [1, 3, 4]
        Explanation: 
        1 -> 3 -> 4 are visible from the right side.
        Level 0: 1
        Level 1: 3 masks 2
        Level 2: 4 masks 5
        """
        root = list_to_tree([1, 2, 3, None, 5, None, 4])
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 4])

    def test_example_2(self):
        """
        Test with a tree that has only right children.
        Input: [1, null, 3]
        Expected Output: [1, 3]
        Explanation: All nodes are on the right side and visible.
        """
        root = list_to_tree([1, None, 3])
        self.assertEqual(self.solution.rightSideView(root), [1, 3])

    def test_example_3(self):
        """
        Test with an empty tree.
        Input: []
        Expected Output: []
        Explanation: No nodes, so result is empty.
        """
        root = list_to_tree([])
        self.assertEqual(self.solution.rightSideView(root), [])

    def test_left_branch_deeper(self):
        """
        Test where the left branch is deeper than the right branch.
        Input: [1, 2, 3, 4]
        Expected Output: [1, 3, 4]
        Explanation:
        Level 0: 1
        Level 1: 3 (right child) masks 2
        Level 2: 4 (left child of 2) is visible because there is no right child at this level.
        """
        root = list_to_tree([1, 2, 3, 4])
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 4])

    def test_single_node(self):
        """
        Test with a single node tree.
        Input: [1]
        Expected Output: [1]
        Explanation: The root is the only visible node.
        """
        root = list_to_tree([1])
        self.assertEqual(self.solution.rightSideView(root), [1])

if __name__ == '__main__':
    unittest.main()
