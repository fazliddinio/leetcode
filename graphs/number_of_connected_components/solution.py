# LeetCode 323: Number of Connected Components in an Undirected Graph
# Time: O(n), Space: O(n)

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for x, y in edges:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        return len(set(find(i) for i in range(n)))
