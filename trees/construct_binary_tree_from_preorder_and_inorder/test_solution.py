import pytest
from .solution import Solution, TreeNode

def test_build_tree():
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    
    root = s.buildTree(preorder, inorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7
