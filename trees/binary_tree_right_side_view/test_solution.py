import pytest
from .solution import Solution, TreeNode

def test_right_side_view():
    s = Solution()
    #    1
    #   / \
    #  2   3
    #   \   \
    #    5   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    
    assert s.rightSideView(root) == [1, 3, 4]
    assert s.rightSideView(None) == []
