from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))

        reorders = 0
        visited = {0}
        queue = deque([0])

        while queue:
            current_city = queue.popleft()
            
            for neighbor, direction in adj[current_city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    
                    if direction == 1:
                        reorders += 1
                        
                    queue.append(neighbor)
                    
        return reorders
