"""
Accounts Merge
LeetCode 721

Approach: Union-Find (Disjoint Set Union)
Time: O(N * K * α(N*K)) ≈ O(N*K) — where N = number of accounts, K = max emails per account.
Space: O(N * K) — for the parent/rank arrays and email-to-owner mapping.
Brute: O(N*K * N*K) — DFS/BFS on email graph, building adjacency list of all emails.
"""

from typing import List
from collections import defaultdict


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                email_to_name[email] = name
                union(account[1], email)

        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        return [[email_to_name[root]] + sorted(emails)
                for root, emails in groups.items()]
