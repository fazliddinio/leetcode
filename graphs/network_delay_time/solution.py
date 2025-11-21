# LeetCode 743: Network Delay Time
# Time: O(E log V), Space: O(V + E)

import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        
        result = max(dist[1:])
        return result if result < float('inf') else -1
