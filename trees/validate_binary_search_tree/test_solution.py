import pytest
from .solution import Solution, TreeNode

def test_is_valid_bst():
    s = Solution()
    
    # Valid:   2
    #         / \
    #        1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert s.isValidBST(root) == True
    
    # Invalid:   5
    #           / \
    #          1   4
    #             / \
    #            3   6
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert s.isValidBST(root) == False
