import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
    print(time.time() - start)

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0

        def dfs(r,c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] != 0:
                res = grid[r][c]
                grid[r][c] = 0
                return res + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    result = max(result, dfs(i,j))
        return result

if __name__ == '__main__':
    sys.exit(main())