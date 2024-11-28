import sys
import time
from collections import deque
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
    print(time.time() - start)

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        #x,y,dist
        queue.append([0,0,0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while queue:
            x,y, dist = queue.popleft()
            if x == m-1 and y == n -1:
                return dist
            
            for dx, dy in directions:
                newx = dx + x
                newy = dy + y
                if newx >= 0 and newx < m and newy >= 0 and newy < n:
                    if not visited[newx][newy]:
                        visited[newx][newy] = True
                        if grid[newx][newy] == 0:
                            queue.appendleft([newx, newy, dist])
                        else:
                            queue.append([newx, newy, dist + 1])



if __name__ == '__main__':
    sys.exit(main())