import pytest
from .solution import Solution, TreeNode

def test_max_depth():
    s = Solution()
    # Correct tree construction for test
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    assert s.maxDepth(root) == 3
    assert s.maxDepth(TreeNode(1)) == 1
    assert s.maxDepth(None) == 0
