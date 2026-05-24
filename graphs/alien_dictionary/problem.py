"""
==========================================
  Alien Dictionary (LeetCode 269)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
There is a new alien language that uses the English alphabet. However, the order among letters are unknown to you.
You are given a list of strings words from the dictionary, where words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no valid ordering, return "".

Example 1: Input: words = ["wrt","wrf","er","ett","rftt"], Output: "wertf"

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
You see an alien dictionary. Deduce their alphabetical order!

    Example: ["wrt", "wrf"]
    Both start with "wr". We see 't' comes before 'f'! So `t -> f`.

Method: Topological Sort on a Graph
  1. Compare adjacent words to build a graph of rules (`t` points to `f`).
  2. Use Kahn's algorithm (indegree counting) or DFS tracking paths to unroll the dependencies.
  3. If you ever hit a cycle (`a -> b` and `b -> a`), it's impossible (return "").
"""
