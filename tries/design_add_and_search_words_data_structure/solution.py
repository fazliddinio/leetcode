"""
Design Add and Search Words Data Structure
LeetCode 211

Approach: Trie + DFS
Time: Add: O(M). Search: O(M) best, O(M * 26^L) worst (wildcards).
Space: O(M * L) — Trie storage (M words, L avg len).
Brute: O(M * L) — Store words in a list, linear scan with regex matching for wildcards.
"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, node, word, idx):
        if idx == len(word):
            return node.is_end_of_word
        char = word[idx]
        if char == '.':
            for child in node.children.values():
                if self._dfs(child, word, idx + 1):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self._dfs(node.children[char], word, idx + 1)
