from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
    print(time.time() - start)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        for a, b in edges:
            visited = set()
            if a in graph and b in graph and dfs(a, b, visited):
                return [a, b]
            graph[a].append(b)
            graph[b].append(a)


if __name__ == '__main__':
    sys.exit(main())