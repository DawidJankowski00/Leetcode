from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {}
        result = []
        for i in range(n-1):
            graph[i] = [i+1]
        for el in queries:
            queue = deque()
            graph[el[0]].append(el[1])
            queue.append([0, 0])
            visited = set()
            visited.add(0)

            while queue:
                q, state = queue.popleft()
                if q == n-1:
                    result.append(state)
                    break
                vs = graph[q]
                for v in vs:
                    if v not in visited:
                        queue.append([v, state+1])
                        visited.add(v)

        return result
