"""
Alien Dictionary
LeetCode 269

Approach: Kahn's Algorithm (BFS)
Time: O(C) — C is total length of all words. Building graph takes O(C). BFS takes O(U+E) where U<=26.
Space: O(1) — Graph size limited to 26 chars.
Brute: O(C + U^2) — DFS-based topological sort with cycle detection via post-order traversal.
"""

from typing import List
from collections import deque


class Solution:

    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = (words[i], words[i + 1])
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ''
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) != len(indegree):
            return ''
        return ''.join(result)
