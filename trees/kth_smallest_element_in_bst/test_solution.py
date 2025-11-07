import pytest
from .solution import Solution, TreeNode

def test_kth_smallest():
    s = Solution()
    #    3
    #   / \
    #  1   4
    #   \
    #    2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    
    assert s.kthSmallest(root, 1) == 1
    assert s.kthSmallest(root, 3) == 3
