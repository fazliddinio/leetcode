"""
Time Based Key-Value Store
LeetCode 981

Approach: Hash Map + Binary Search
Time: set: O(1), get: O(log n) — binary search on timestamps
Space: O(n) — store all entries
Brute: O(n) — linear scan backwards through timestamps for each get
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
                
        return res
