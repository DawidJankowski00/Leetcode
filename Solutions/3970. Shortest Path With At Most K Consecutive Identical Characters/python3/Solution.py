from collections import defaultdict
import heapq
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if k < 1:
            return -1

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        start_char = labels[0]
        min_dist = {(0, start_char, 1): 0}
        pq = [(0, 0, start_char, 1)]

        while pq:
            cost, u, last_char, streak = heapq.heappop(pq)

            if u == n - 1:
                return cost

            if cost > min_dist.get((u, last_char, streak), float("inf")):
                continue

            for v, weight in graph[u]:
                next_char = labels[v]
                new_streak = streak + 1 if next_char == last_char else 1

                if new_streak <= k:
                    new_cost = cost + weight
                    state = (v, next_char, new_streak)

                    if new_cost < min_dist.get(state, float("inf")):
                        min_dist[state] = new_cost
                        heapq.heappush(pq, (new_cost, v, next_char, new_streak))

        return -1