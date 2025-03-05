import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.coloredCells(3))
    print(time.time() - start)

class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n-1) + 1
        

if __name__ == '__main__':
    sys.exit(main())