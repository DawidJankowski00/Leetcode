import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.checkIfPrerequisite(2,[[1,0]],[[0,1],[1,0]]))
    print(time.time() - start)

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]

        for pre in prerequisites:
            reachable[pre[0]][pre[1]] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        return [reachable[u][v] for u, v in queries]
        

if __name__ == '__main__':
    sys.exit(main())