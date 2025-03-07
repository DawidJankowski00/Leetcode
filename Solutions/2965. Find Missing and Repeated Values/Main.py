import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))
    print(time.time() - start)

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        tab = {}
        result = []
        for i in grid:
            for j in i:
                if j in tab:
                    result.append(j)
                tab[j] = True
        for i in range(1, n*n + 1):
            if i in tab:
                continue
            else:
                result.append(i)
                break
        return result
        

if __name__ == '__main__':
    sys.exit(main())