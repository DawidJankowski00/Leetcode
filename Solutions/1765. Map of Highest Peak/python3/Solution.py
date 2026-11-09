from collections import deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.highestPeak([[0,1],[0,0]]))
    print(time.time() - start)

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        result = [[-1] * m for _ in range(n)]
        queue = deque()


        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))

        return result
        

if __name__ == '__main__':
    sys.exit(main())