import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
    print(time.time() - start)

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0
        for i in range(n):
            curr_row, col = 0, -1
            for j in range(m):
                if grid[i][j]:
                    curr_row += 1
                    col = j
            if curr_row == 1:
                for r in range(n):
                    if r != i and grid[r][col]:
                        result += 1
                        break
            else:
                result += curr_row
        return result
            

        

if __name__ == '__main__':
    sys.exit(main())