from collections import defaultdict


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 1_000_000_007
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        deph = self.dfs(tree, 1, -1)
        return pow(2, deph - 2, mod)
    def dfs(self, tree, curr, parent) -> int:
        max_child_depth = 0
        
        for v in tree[curr]:
            if v == parent:
                continue
            
            child_depth = self.dfs(tree, v, curr)
            if child_depth > max_child_depth:
                max_child_depth = child_depth
                
        return 1 + max_child_depth
        