import pytest
from .solution import Solution, TreeNode

def test_lowest_common_ancestor():
    s = Solution()
    # Tree:    6
    #        /   \
    #       2     8
    #      / \   / \
    #     0   4 7   9
    #        / \
    #       3   5
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    n2 = root.left
    n8 = root.right
    n2.left = TreeNode(0)
    n4 = TreeNode(4)
    n2.right = n4
    
    assert s.lowestCommonAncestor(root, n2, n8).val == 6
    assert s.lowestCommonAncestor(root, n2, n4).val == 2
