from collections import defaultdict, deque
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n == 1:
            return 1
        result = 0
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        Q = deque()

        for v in graph.keys():
            if len(graph[v]) == 1:
                Q.append(v)
        while Q:
            node = Q.popleft()
            if graph[node]:
                parent = graph[node].pop()
                graph[parent].remove(node)
                if len(graph[parent]) == 1:
                    Q.append(parent)
                if values[node] % k == 0:
                    result += 1
                else:
                    values[parent] += values[node]
            else:
                result += 1
        return result
