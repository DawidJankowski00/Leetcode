from collections import deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.largestIsland([[1,0],[0,1]]))
    print(time.time() - start)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        result = 0
        grup = 2
        grups = {}
        def dfs(r,c):
            if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = grup
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            else:
                return 0
            
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros.append((i,j))
                elif grid[i][j] == 1:
                    tmp = dfs(i,j)
                    if tmp > result:
                        result = tmp
                    grups[grup] = tmp
                    grup += 1
        if result == 0:
            return 1
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r,c in zeros:
            tmp = 1
            visited = []
            for x,y in directions:
                newr = r+x
                newc = c+y
                if 0 <= newr < n and 0 <= newc < n and grid[newr][newc] != 0:
                    if grid[newr][newc] not in visited:
                        visited.append(grid[newr][newc])
                        tmp += grups[grid[newr][newc]]
            if tmp > result:
                result = tmp
        return result

        
        


if __name__ == '__main__':
    sys.exit(main())