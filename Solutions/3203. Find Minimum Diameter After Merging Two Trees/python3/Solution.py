from collections import defaultdict, deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minimumDiameterAfterMerge([[0,1],[0,2],[0,3]],[[0,1]]))
    print(time.time() - start)

class Solution:
    def tree_diameter(self, edges):
        if not edges:
            return 0
        def bfs(start):
            visited = [-1] * len(graph)
            queue = deque([start])
            visited[start] = 0
            farthest_node, max_distance = start, 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = visited[node] + 1
                        queue.append(neighbor)
                        if visited[neighbor] > max_distance:
                            farthest_node, max_distance = neighbor, visited[neighbor]
            
            return farthest_node, max_distance

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        farthest_node, _ = bfs(0)

        _, diameter = bfs(farthest_node)

        return diameter
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        D1 = self.tree_diameter(edges1)
        D2 = self.tree_diameter(edges2)
        return max(D1, D2, (D1+1)//2+(D2+1)//2+1)
        

if __name__ == '__main__':
    sys.exit(main())