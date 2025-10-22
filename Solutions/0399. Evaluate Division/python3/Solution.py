from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = (1/values[i])
        visited = []
        def dfs(a, curr, res):
            graph[a][curr] = res
            graph[curr][a] = 1/ res
            visited.append(curr)
            
            for v in list(graph[curr].keys()):
                if v not in visited:
                    dfs(a, v, res * graph[curr][v])
                    
        for v in list(graph.keys()):
            visited = []
            dfs(v, v, 1.0)
        result = []
        for a, b in queries:
            if a in graph:
                if b in graph[a]:
                    result.append(graph[a][b])
                    continue
            
            result.append(-1.0)
        return result