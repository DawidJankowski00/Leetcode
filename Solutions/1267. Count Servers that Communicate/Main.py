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
        for i in range(0, n):
            first = (0, 0)
            is_first_updated = False
            curr_row = 0
            for j in range(0, m):
                if grid[i][j]:
                    curr_row += 1
                    if curr_row >= 2:
                        if not is_first_updated:
                            is_first_updated = True
                            grid[first[0]][first[1]] = -1
                            result += 1
                        result += 1
                        grid[i][j] = -1
                    else:
                        first = (i, j)
        for i in range(0, m):
            curr_col = 0
            not_counted = 0
            for j in range(0, n):
                if grid[j][i] == 1 or grid[j][i] == -1:
                    if grid[j][i] == 1:
                        not_counted += 1
                    curr_col += 1
            if curr_col >= 2:
                result += not_counted
        return result

        

if __name__ == '__main__':
    sys.exit(main())