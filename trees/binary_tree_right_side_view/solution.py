"""
Binary Tree Right Side View
LeetCode 199

Approach: BFS (Level Order)
Time: O(n) — Visit every node once.
Space: O(n) — Queue width (or O(h) with DFS).
Brute: O(n) — Recursive DFS visiting right subtree first, recording first node at each depth.
"""

from typing import Optional, List
from collections import deque


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
