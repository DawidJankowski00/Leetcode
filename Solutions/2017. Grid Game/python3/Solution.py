import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.gridGame([[1,3,1,15],[1,3,3,1]]))
    print(time.time() - start)

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        lsum = 0
        rsum = sum(grid[0])
        maxpoints = rsum

        for i in range(0, n):
            
            rsum -= grid[0][i]
            maxpoints = min(maxpoints, max(lsum, rsum))
            lsum += grid[1][i]
        return maxpoints

        

if __name__ == '__main__':
    sys.exit(main())