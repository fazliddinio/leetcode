import pytest
from .solution import Solution, TreeNode

def test_max_path_sum():
    s = Solution()
    
    #   -10
    #   /  \
    #  9   20
    #     /  \
    #    15   7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    assert s.maxPathSum(root) == 42 # 15 + 20 + 7
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert s.maxPathSum(root) == 6
