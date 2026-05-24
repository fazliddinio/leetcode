import unittest
from solution import Solution, TreeNode

class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests the example case [1,2,3,4,5]."""
        # Construct tree:
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        expected = 3  # Path: 4->2->1->3 or 5->2->1->3
        self.assertEqual(self.solution.diameterOfBinaryTree(root), expected)

    def test_example_2(self):
        """Tests the example case [1,2]."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        expected = 1
        self.assertEqual(self.solution.diameterOfBinaryTree(root), expected)

    def test_single_node(self):
        """Tests a single node tree."""
        root = TreeNode(1)
        expected = 0
        self.assertEqual(self.solution.diameterOfBinaryTree(root), expected)
        
    def test_empty_tree(self):
        """Tests an empty tree (None)."""
        root = None
        expected = 0
        self.assertEqual(self.solution.diameterOfBinaryTree(root), expected)

if __name__ == '__main__':
    unittest.main()
