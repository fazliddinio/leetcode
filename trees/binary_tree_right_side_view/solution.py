# LeetCode 199: Binary Tree Right Side View
# Time: O(n), Space: O(n)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return result
