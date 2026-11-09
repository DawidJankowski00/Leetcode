from collections import deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(time.time() - start)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue = deque()
                    result += 1
                    queue.append((i,j))
                    while queue:
                        x, y = queue.popleft()
                        grid[x][y] = 0
                        for x1, y1 in directions:
                            nx = x + x1
                            ny = y + y1
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                grid[nx][ny] = 0
                                queue.append((nx, ny))
        return result

if __name__ == '__main__':
    sys.exit(main())