import pytest
from .solution import Codec, TreeNode

def test_serialize_deserialize():
    c = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    data = c.serialize(root)
    assert isinstance(data, str)
    
    new_root = c.deserialize(data)
    assert new_root.val == 1
    assert new_root.right.right.val == 5
