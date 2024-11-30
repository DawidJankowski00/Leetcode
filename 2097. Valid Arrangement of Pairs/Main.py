from collections import defaultdict
import sys
import time
import copy
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.validArrangement([[5,1],[4,5],[11,9],[9,4]]))
    print(time.time() - start)

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)
        for v in pairs:
            graph[v[0]].append(v[1])
            inOutDeg[v[0]] += 1
            inOutDeg[v[1]] -= 1
        
        startNode = pairs[0][0] 
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break
        path = []
        def dfs(u):
            while graph[u]:
                v = graph[u].pop()
                dfs(v)
                path.append([u, v])
        dfs(startNode)

        return path[::-1]
        

if __name__ == '__main__':
    sys.exit(main())