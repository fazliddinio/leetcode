# LeetCode 572: Subtree of Another Tree
# Time: O(m * n), Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return same(p.left, q.left) and same(p.right, q.right)
        
        if not root:
            return False
        if same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
