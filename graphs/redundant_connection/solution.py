# LeetCode 684: Redundant Connection
# Time: O(n), Space: O(n)

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for x, y in edges:
            px, py = find(x), find(y)
            if px == py:
                return [x, y]
            parent[px] = py
        
        return []
