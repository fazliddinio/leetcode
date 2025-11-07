import pytest
from .solution import Solution, TreeNode

def test_is_subtree():
    s = Solution()
    
    # Root: 3,4,5,1,2
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    
    # SubRoot: 4,1,2
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    
    assert s.isSubtree(root, subRoot) == True
    
    subRoot.right.left = TreeNode(0) # Change structure
    assert s.isSubtree(root, subRoot) == False
