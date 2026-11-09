from collections import deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
    print(time.time() - start)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        
        visited = [0] * n
        groups = []
        
        for i in range(n):
            if not visited[i]: 
                stack = [i]
                visited[i] = 1
                group = [i]
                
                while stack: 
                    u = stack.pop()
                    for v in graph[u]: 
                        if not visited[v]: 
                            visited[v] = visited[u] + 1
                            stack.append(v)
                            group.append(v)
                        elif (visited[u] % 2) == (visited[v] % 2):
                            return -1
                
                groups.append(group)
        
        def bfs(start):
            max_depth = 0
            visited = set([start])
            queue = deque([start])
            
            while queue: 
                max_depth += 1
                for _ in range(len(queue)): 
                    node = queue.popleft()
                    for neighbor in graph[node]: 
                        if neighbor not in visited: 
                            visited.add(neighbor)
                            queue.append(neighbor)
            return max_depth
        
        return sum(max(bfs(node) for node in group) for group in groups)
        

if __name__ == '__main__':
    sys.exit(main())