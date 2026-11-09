from heapq import heappop, heappush
import sys
import time
from collections import deque
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minimumTime([[0,1,3,2],[5,1,2,5],[4,3,8,6]]))
    print(time.time() - start)

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m = len(grid)
        n = len(grid[0])
        visited = [[False]* n for _ in range(m)]
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        heap = [(0,0,0)]
        while heap:
            t, x,y = heappop(heap)
            if x == m-1 and y == n-1:
                return t
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                newx = dx + x
                newy = dy + y
                if 0 <= newx < m and 0 <= newy < n:
                    if visited[newx][newy] == False:
                        wait = (grid[newx][newy] - t) % 2 == 0
                        nt = max(grid[newx][newy] + wait, t + 1)
                        heappush(heap, (nt, newx, newy))
        return -1

if __name__ == '__main__':
    sys.exit(main())