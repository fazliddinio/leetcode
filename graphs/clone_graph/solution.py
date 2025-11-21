# LeetCode 133: Clone Graph
# Time: O(n), Space: O(n)

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        
        clones = {}
        
        def dfs(n):
            if n in clones:
                return clones[n]
            
            clone = Node(n.val)
            clones[n] = clone
            
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
