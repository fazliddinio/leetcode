"""
Minimum Depth of Binary Tree
LeetCode 111

Approach: BFS (Level Order)
Time: O(n) — Visit nodes until leaf found.
Space: O(n) — Queue width (max n/2).
Brute: O(n) — Recursive DFS exploring all paths, return shortest depth.
"""

from typing import Optional
from collections import deque


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and (not node.right):
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
