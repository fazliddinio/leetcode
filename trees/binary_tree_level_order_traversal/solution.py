"""
Binary Tree Level Order Traversal
LeetCode 102

Approach: BFS (Queue)
Time: O(n) — Visit every node once.
Space: O(n) — Queue can hold up to n/2 nodes (max width).
Brute: O(n) — Recursive DFS passing depth to bucket nodes by level.
"""

from typing import Optional, List
from collections import deque


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
