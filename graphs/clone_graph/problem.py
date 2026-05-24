"""
==========================================
  Clone Graph (LeetCode 133)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Make an EXACT copy of a spider web (graph) without tying your new web to the old one.

Method: DFS or BFS with a Hash Map.
  1. Map `old_node` to `new_node (val)`.
  2. Start traversing the old graph.
  3. For every neighbor of a node: If neighbor is not in the map, create it and visit it!
  4. Link the new node's neighbors to the cloned neighbors in the map.
"""
