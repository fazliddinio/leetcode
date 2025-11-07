import pytest
from .solution import Solution, TreeNode

def test_level_order():
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert s.levelOrder(None) == []
