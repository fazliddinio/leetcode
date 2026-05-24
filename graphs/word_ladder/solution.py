"""
Word Ladder
LeetCode 127

Approach: BFS with Pattern Hashing
Time: O(M^2 * N) — M is word length, N is number of words. Preprocessing takes M^2*N.
Space: O(M^2 * N) — Dictionary storing patterns.
Brute: O(26 * M * N) — BFS trying all 26 letter replacements at each position per word.
"""

from typing import List
from collections import defaultdict, deque


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i + 1:]
                patterns[pattern].append(w)
        visited = set([beginWord])
        queue = deque([beginWord])
        length = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neighbor in patterns[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                    patterns[pattern] = []
            length += 1
        return 0
