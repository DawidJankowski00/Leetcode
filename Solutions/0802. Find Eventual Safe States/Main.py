import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
    print(time.time() - start)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        result = []
        safe = {}
        def visit_node(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for v in graph[i]:
                if not visit_node(v):
                    return False
            safe[i] = True
            return True

        for i in range(len(graph)):
            if visit_node(i):
                result.append(i)

        return result

if __name__ == '__main__':
    sys.exit(main())