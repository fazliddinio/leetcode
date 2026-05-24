"""
Task Scheduler
LeetCode 621

Approach: Greedy (Math / Count)
Time: O(N) — Single pass to count frequencies. Sorting takes O(26 log 26) = O(1).
Space: O(1) — 26 lowercase letters.
Brute: O(T * 26) — Heap simulation picking most frequent available task each time slot.
"""

from typing import List
from collections import Counter


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        max_freq_count = sum((1 for v in count.values() if v == max_freq))
        part_count = max_freq - 1
        part_length = n - (max_freq_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_freq * max_freq_count
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles
