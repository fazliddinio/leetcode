import pytest
from .solution import Solution, TreeNode

def test_invert_tree():
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    inv = s.invertTree(root)
    assert inv.val == 2
    assert inv.left.val == 3
    assert inv.right.val == 1
    
    assert s.invertTree(None) == None
