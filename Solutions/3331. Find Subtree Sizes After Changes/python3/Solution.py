from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26

        def dfs_find_parents(u: int):
            char_idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[char_idx]

            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor

            last_seen[char_idx] = u

            for v in adj[u]:
                dfs_find_parents(v)

            last_seen[char_idx] = prev_ancestor

        dfs_find_parents(0)

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        answer = [1] * n

        def dfs_calc_sizes(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += dfs_calc_sizes(v)
            answer[u] = size
            return size

        dfs_calc_sizes(0)

        return answer